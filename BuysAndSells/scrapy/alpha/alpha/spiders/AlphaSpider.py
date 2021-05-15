import scrapy,re,datetime

#  Left off creating regular expressions for each type of timestamp

class AlphaSpider(scrapy.Spider):
    name = 'alphaScrape'

    start_urls = [
        'file:///Users/none/Desktop/Sort/MISC/Python/exercises/github/Python/BuysAndSells/scrapy/alpha/alpha/page1.html'
        # 'https://seekingalpha.com/market-news/m-a'
    ]

    def convertTimestamp(self,timestamp):

        #  Timestamp one regex. ex) Mar. 21, 2019, 1:26 AM
        timestamp_one = re.compile('\w{3}\. \d{1,2}, \d{4}, \d{1,2}:\d{1,2} (AM|PM)')

        #  Timestamp two regex. ex) Thu, Apr. 22, 4:56 PM
        timestamp_two = re.compile('\w{3}, \w{3}\. \d{1,2}\, \d{1,2}:\d{2} (AM|PM)')

        #  Timestamp three ex) Yesterday or Today
        timestamp_three = re.compile('Yesterday|Today')

        if timestamp_one.match(timestamp):
            datetime_object = datetime.datetime.strptime(timestamp,
                                                         "%b. %d, %Y, %I:%M %p")
            return datetime_object
        elif timestamp_two.match(timestamp):
            datetime_object = datetime.datetime.strptime(timestamp,
                                                         "%a, %b. %d, %I:%M %p")
            #  Changing year to the current year.
            datetime_object = datetime_object.replace(year=
                                                      datetime.datetime
                                                      .now().year)
            return datetime_object
            # print('Found second type of timestamp')
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


    # def databaseInsert(self,data_entries):
    #
    #     pass


    def parse(self, response):

        base_url = 'https://seekingalpha.com'

        #  Formats of date
        #  Mar. 21, 2019, 1:26 PM regex = \w{3}\. \d{1,2}, \d{4}, \d{1,2}:\d{1,2} \W{2}')
        #  Thu, Apr. 22, 4:56 PM
        #  Today

        # my_date = datetime.datetime.strptime(my_string, "%a, %b. %d, %I:%M %p")

        #     #  For loop to grab reported information for each sell or buy.
        for sel in response.xpath('//ul/li[@class="mc"]'):

            #  This will grab the date from the reported sell or buy.
            date = self.getEntry('date',sel)

            #  Getting stock symbol
            symbol = self.getEntry('symbol', sel)

            #  This will grab the title of the reported sell or buy.
            title = self.getEntry('title', sel)

            #  This will grab the link to the reported sell or buy.
            link = self.getEntry('link', sel)

            # print([date,symbol,title,link])

            data_entries_dictionary = {
                'date': date,
                'symbol': symbol,
                'title': title,
                'link': link
            }

            print(self.convertTimestamp(date))

            #  Inserting entries in database.
            # self.databaseInsert(data_entries_dictionary)

        # for sel in response.xpath('//ul/li[@class="mc"]/div[@class="media-body"]/div[@class="title"]'):

        #  Getting next link
        # next_link = base_url + \
        #             response.xpath('//ul[@class="list-inline"]/li[@class="next"]/a/@href').extract()[0]
        #
        #
        # print('On page: ' + next_link)
        # if next_link is not None:
        #     print('in here')
        #     time.sleep(10)
        #     yield response.follow(next_link,callback=self.parse)