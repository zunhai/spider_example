import time
import re
import scrapy
from scrapy import Selector
from newSpider.items import NewspiderItem


class ArticleSpider(scrapy.Spider):

    name = "article"

    def __init__(self):
        self.server_link = 'http://www.biqukan.com/'
        self.allowed_domains = [ "www.biqukan.com" ]
        self.start_urls = "http://www.biqukan.com/10_10350/"


    def start_requests(self):
        yield scrapy.Request(url = self.start_urls , callback=self.parse1)

    def parse1(self , response):
        items = []
        
        
        scl = Selector(response)
        
        zhangjie_urls = scl.xpath('//dd/a/@href').extract()

        zhangjie_names = scl.xpath('//dd/a[1]/text()').extract()

        for index in range(len(zhangjie_urls)):
            item = NewspiderItem()
            

            item["zhangjie_url"] = self.server_link + zhangjie_urls[index]

            item["zhangjie_name"] = zhangjie_names[index]

            items.append(item)

        for item in items[0:]:
            yield scrapy.Request(url = item['zhangjie_url'], meta = {'item':item}, callback = self.parse2)

        time.sleep(2)


    def parse2(self , response):
        item = response.meta["item"]
        item["zhangjie_url"] = response.url
        scl = Selector(response)
        txt = scl.xpath("//div[@id='content']/text()").extract()
        item["txt"] = txt;

        yield item
        time.sleep(2)


