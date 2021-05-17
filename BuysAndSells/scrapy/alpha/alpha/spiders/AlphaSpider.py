import scrapy,re,datetime,random,time
from ..db_interaction import db_interaction
from ..config import config

#  Left off creating regular expressions for each type of timestamp

class AlphaSpider(scrapy.Spider):
    name = 'alphaScrape'

    # https://seekingalpha.com/market-news/m-a?page=1
    # start_urls = ["https://seekingalpha.com/market-news/m-a?page=%s" % page for page in
    #               list(range(1,100))]

    start_urls = [
        # 'file:///Users/none/Desktop/Sort/MISC/Python/exercises/github/Python/BuysAndSells/scrapy/alpha/alpha/page2.html'
        'https://seekingalpha.com/market-news/m-a'
    ]

    def convertTimestamp(self,timestamp):

        #  Timestamp one regex. ex) Mar. 21, 2019, 1:26 AM
        timestamp_one = re.compile('\w{3}\. \d{1,2}, \d{4}, \d{1,2}:\d{1,2} (AM|PM)')

        #  Timestamp two regex. ex) Thu, Apr 22, 4:56 PM
        timestamp_two = re.compile('\w{3}, \w{3} \d{1,2}\, \d{1,2}:\d{2} (AM|PM)')

        #  Timestamp three ex) Yesterday
        timestamp_three = re.compile('Yesterday, (\d{1,2}:\d{2} (AM|PM))')


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

        elif timestamp_three.match(timestamp):

            #  Settings days timedelta of 1 day
            days = datetime.timedelta(1)

            #  Getting todays date in format 2021-05-14
            todays_date = datetime.datetime.now().date()

            #  Subtracting one day from current date
            yesterdays_date = str(todays_date - days)
            #  Getting time from the timestamp found.
            yesterdays_time = timestamp_three.match(timestamp).group(1)

            #  Getting final timestamp string.
            yesterdays_timestamp = yesterdays_date + ' ' + yesterdays_time

            # yesterdays_timestamp = '2021-05-14 12:53 AM'

            #  Getting final datetime object
            yesterdays_datetime_object = datetime.datetime.strptime(
                yesterdays_timestamp,"%Y-%m-%d %I:%M %p")

            return yesterdays_datetime_object.strftime("%Y-%m-%d %H:%M:%S")

        else:
            return timestamp

        #  Example timestamp
        # timestamp_one.match('Mar. 21, 2019, 1:26 AM').group()
        # Tue, Apr. 13, 9:52 AM

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

        # print(data_entries)

        db_interaction_object = db_interaction('127.0.0.1',
                                               config.username,
                                               config.password)
        #  Connecting to database
        db_interaction_object.connect()

        #  Inserting data into table
        db_interaction_object.insert(table='transactions',data=data_entries)

    def parse(self, response):

        base_url = 'https://seekingalpha.com'

        page_number = response.url.split("/")[-1][-1]
        filename = 'page' + page_number + '.html'
        # filename = response.url.split("/")[-1] + '.html'
        with open(filename, 'wb') as f:
            f.write(response.body)

        #  Closing file handler
        f.close()

        #  Formats of date
        #  Mar. 21, 2019, 1:26 PM regex = \w{3}\. \d{1,2}, \d{4}, \d{1,2}:\d{1,2} \W{2}')
        #  Thu, Apr. 22, 4:56 PM
        #  Today

        # my_date = datetime.datetime.strptime(my_string, "%a, %b. %d, %I:%M %p")

        #     #  For loop to grab reported information for each sell or buy.
        # for sel in response.xpath('//ul/li[@class="mc"]'):
        #
        #     #  This will grab the date from the reported sell or buy.
        #     date = self.getEntry('date',sel)
        #
        #     #  Getting stock symbol
        #     symbol = self.getEntry('symbol', sel)
        #
        #     #  This will grab the title of the reported sell or buy.
        #     title = self.getEntry('title', sel)
        #
        #     #  This will grab the link to the reported sell or buy.
        #     link = self.getEntry('link', sel)
        #
        #     #  This will be the page url
        #     page_url = response.request.url
        #
        #     # print([date,symbol,title,link,page_url])
        #
        #     data_entries_dictionary = {
        #         'date': self.convertTimestamp(date),
        #         'symbol': symbol,
        #         'title': title,
        #         'link': link,
        #         'page_url': response.request.url
        #     }
        #
        #
        #     #  Inserting entries in database.
        #     self.databaseInsert(data_entries_dictionary)

        # for sel in response.xpath('//ul/li[@class="mc"]/div[@class="media-body"]/div[@class="title"]'):

        #  Getting next link
        next_link = base_url + \
                    response.xpath('//ul[@class="list-inline"]/li[@class="next"]/a/@href').extract()[0]
        #
        #
        print('On page: ' + next_link)
        if next_link is not None:
            #  Sleeping for 20 seconds
            time.sleep(20)
            yield response.follow(next_link,callback=self.parse)