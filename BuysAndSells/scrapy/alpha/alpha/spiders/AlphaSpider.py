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

        if timestamp_one.match(timestamp_one):
            datetime_object = datetime.datetime.strptime(timestamp, "%b. %d, %Y, %I:%M %p")

            #  convert timestamp here.

        #  Example timestamp
        timestamp_one.match('Mar. 21, 2019, 1:26 AM').group()


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
            date = sel.xpath('div[@class="media-body"]/div[@class="mc-share-info"]/span[@class="item-date"]/text()').get()

            #  Getting stock symbol
            symbol = sel.xpath('div[@class="media-left"]/a/text()').extract()[0]

            #  This will grab the title of the reported sell or buy.
            title = sel.xpath('div[@class="media-body"]/div[@class="title"]/a/text()').extract()[0]

            #  This will grab the link to the reported sell or buy.
            link = sel.xpath('div[@class="media-body"]/div[@class="title"]/a/@href').extract()[0]

            print([date,symbol,title,link])
            # print((date,title,link))

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