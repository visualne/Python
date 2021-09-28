import scrapy,re,datetime, time
from .extras.db_interaction import db_interaction
from .extras.config import config

#  Need to escape ' from title strings.

class AlphaSpider(scrapy.Spider):
    name = 'alphaScrape'

    start_urls = [
        'https://seekingalpha.com/market-news/m-a'
    ]

    def convertTimestamp(self,timestamp):

        #  Timestamp one regex. ex) Mar. 21, 2019, 1:26 AM
        timestamp_one = re.compile('\w{3}\. \d{1,2}, \d{4}, \d{1,2}:\d{1,2} (AM|PM)')

        #  Timestamp two regex. ex) Thu, Apr 22, 4:56 PM
        timestamp_two = re.compile('\w{3}, \w{3} \d{1,2}\, \d{1,2}:\d{2} (AM|PM)')

        #  Timestamp three regex ex) Thu, Apr. 1, 4:41 AM
        timestamp_three = re.compile('\w{3}, \w{3}\. \d{1,2}\, \d{1,2}:\d{2} (AM|PM)')

        #  Timestamp four regex ex) Yesterday
        timestamp_four = re.compile('Yesterday, (\d{1,2}:\d{2} (AM|PM))')

        #  Timestamp five regex ex) Today
        timestamp_five = re.compile('Today, (\d{1,2}:\d{2} (AM|PM))')


        if timestamp_one.match(timestamp):
            datetime_object = datetime.datetime.strptime(timestamp,
                                                         "%b. %d, %Y, %I:%M %p")

            return datetime_object.strftime("%Y-%m-%d %H:%M:%S")

        elif timestamp_two.match(timestamp):
            datetime_object = datetime.datetime.strptime(timestamp,
                                                         "%a, %b %d, %I:%M %p")
            #  Changing year to the current year.
            datetime_object = datetime_object.replace(year=
                                                      datetime.datetime
                                                      .now().year)

            return datetime_object.strftime("%Y-%m-%d %H:%M:%S")

        # Thu, Apr. 1, 4:41AM
        elif timestamp_three.match(timestamp):
            datetime_object = datetime.datetime.strptime(timestamp,
                                                         "%a, %b. %d, %I:%M %p")
            #  Changing year to the current year.
            datetime_object = datetime_object.replace(year=
                                                      datetime.datetime
                                                      .now().year)

            return datetime_object.strftime("%Y-%m-%d %H:%M:%S")

        elif timestamp_four.match(timestamp):

            #  Settings days timedelta of 1 day
            days = datetime.timedelta(1)

            #  Getting todays date in format 2021-05-14
            todays_date = datetime.datetime.now().date()

            #  Subtracting one day from current date
            yesterdays_date = str(todays_date - days)
            #  Getting time from the timestamp found.
            yesterdays_time = timestamp_four.match(timestamp).group(1)

            #  Getting final timestamp string.
            yesterdays_timestamp = yesterdays_date + ' ' + yesterdays_time

            # yesterdays_timestamp = '2021-05-14 12:53 AM'

            #  Getting final datetime object
            yesterdays_datetime_object = datetime.datetime.strptime(
                yesterdays_timestamp,"%Y-%m-%d %I:%M %p")

            return yesterdays_datetime_object.strftime("%Y-%m-%d %H:%M:%S")

        elif timestamp_five.match(timestamp):

            #  Getting today's date in format 2021-05-14
            todays_date = str(datetime.datetime.now().date())

            todays_time = timestamp_five.match(timestamp).group(1)

            #  Getting final timestamp string.
            todays_timestamp = todays_date + ' ' + todays_time

            todays_datetime_object = datetime.datetime.strptime(
                todays_timestamp,"%Y-%m-%d %I:%M %p")

            return todays_datetime_object.strftime("%Y-%m-%d %H:%M:%S")

        else:
            return timestamp

    def getEntry(self,type_of_data,sel):

        xpathDictionary = {
            'date': 'div[@class="media-body"]/div[@class="mc-share-info"]\
            /span[@class="item-date"]/text()',
            'symbol': 'div[@class="media-left"]/a/text()',
            'title': 'div[@class="media-body"]/div[@class="title"]/a/text()',
            'link': 'div[@class="media-body"]/div[@class="title"]/a/@href'
        }

        #  Attempting to pull data from page.
        try:
            return sel.xpath(xpathDictionary[type_of_data]).extract()[0]
        #  If this except statement is hit it means no data was found.
        except:
            return 'none'


    def databaseInsert(self,data_entries):

        db_interaction_object = db_interaction('127.0.0.1',
                                               config.username,
                                               config.password)
        #  Connecting to database
        db_interaction_object.connect()

        #  Inserting data into table
        db_interaction_object.insert(table='transactions',data=data_entries)

    def parse(self, response):

        base_url = 'https://seekingalpha.com'

        #  For loop to grab reported information for each sell or buy.
        for sel in response.xpath('//ul/li[@class="mc"]'):

            #  This will grab the date from the reported sell or buy.
            date = self.getEntry('date',sel)

            #  Getting stock symbol
            symbol = self.getEntry('symbol', sel)

            #  This will grab the title of the reported sell or buy.
            title = self.getEntry('title', sel)

            #  This will grab the link to the reported sell or buy.
            link = self.getEntry('link', sel)

            #  This will be the page url
            page_url = response.request.url

            #  Creating data dictionary that will be passed to the database.
            data_entries_dictionary = {
                'date': self.convertTimestamp(date),
                'symbol': symbol,
                'title': title,
                'link': link,
                'page_url': response.request.url
            }


            #  Inserting entries in database.
            self.databaseInsert(data_entries_dictionary)

        #  Getting next link
        next_link = base_url + \
                    response.xpath('//ul[@class="list-inline"]/li[@class="next"]/a/@href').extract()[0]


        print('On page: ' + next_link)
        if next_link is not None:
            #  Sleeping for 20 seconds
            time.sleep(20)
            yield response.follow(next_link,callback=self.parse)