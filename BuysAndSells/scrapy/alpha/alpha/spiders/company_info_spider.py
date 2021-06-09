import scrapy
from extras.db_interaction import db_interaction
from extras.config import config



#  Left off trying to understand why the above import won't work.


class CompanyInfoSpiderSpider(scrapy.Spider):
    name = 'company_info_spider'
    allowed_domains = ['seekingalpha.com']
    start_urls = ['https://seekingalpha.com/symbol/LHX']

    def parse(self, response):

        filename = response.url.split("/")[-1] + '.html'
        with open(filename, 'wb') as f:
            f.write(response.body)
