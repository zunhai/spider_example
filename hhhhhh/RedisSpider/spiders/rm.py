# -*- coding: utf-8 -*-
import scrapy
# from scrapy import Request
from scrapy_redis.spiders import RedisSpider
from RedisSpider.items import RedisspiderItem
from scrapy_redis.scheduler import Scheduler
countArray = []

class RmSpider(RedisSpider):
    name = 'rm'

    # allowed_domains = ['tianqi.com']
    # start_urls = ['http://lishi.tianqi.com/']

    # 设置redis_key获取起始的url
    redis_key = 'tianqi'

    # 设置动态获取允许的域
    def __init__(self, *args, **kwargs):
        # Dynamically define the allowed domains list.
        domain = kwargs.pop('domain', '')
        self.allowed_domains = list(filter(None, domain.split(',')))
        # print('------', self.allowed_domains)
        super(RmSpider, self).__init__(*args, **kwargs)

    def parse(self, response):
        # 获取城市列表节点
        city_node_list = response.xpath("//ul[contains(@class,'city')]/li[position()>1]/a")
        # print(len(city_node_list))
        # 遍历获取数据
        for node in city_node_list:
            temp = {}
            temp['city'] = node.xpath('./text()').extract_first()
            temp['city_url'] = node.xpath('./@href').extract_first()
            # 返回城市详情页url继续处理
            yield scrapy.Request(temp['city_url'], callback=self.parse_city_url, meta={'meta_1': temp})

    def parse_city_url(self, response):
        # 获取月份分类节点列表
        month_node_list = response.xpath('//div[@id="tool_site"]/div[2]/ul/li/a')
        # print(len(month_node_list))
        temp = response.meta['meta_1']
        # 遍历获取数据
        for node in month_node_list:
            temp1 = {}
            temp1['city'] = temp['city']
            temp1['city_url'] = temp['city_url']
            # 以上是接收的参数
            temp1['month'] = node.xpath('./text()').extract_first()
            temp1['month_url'] = node.xpath('./@href').extract_first()
            # 返回详情页url继续处理
            yield scrapy.Request(temp1['month_url'], callback=self.parse_detail_url, meta={'meta_2': temp1})

    def parse_detail_url(self, response):
        # 获取详情信息节点列表
        detail_node_list = response.xpath('//div[@id="tool_site"]/div[2]/ul[position()>1]')
        # print('detail_node_list------', len(detail_node_list))
        temp = response.meta['meta_2']

        # print(item)
        # 遍历获取详情信息
        for node in detail_node_list:
            item = RedisspiderItem()
            item['city'] = temp['city']
            item['city_url'] = temp['city_url']
            item['month'] = temp['month']
            item['month_url'] = temp['month_url']
            # 以上是接收的参数
            item['date'] = node.xpath('./li/a/text()').extract_first()
            item['high_tem'] = node.xpath('./li[2]/text()').extract_first()
            item['low_tem'] = node.xpath('./li[3]/text()').extract_first()
            item['weather'] = node.xpath('./li[4]/text()').extract_first()
            item['w_direc'] = node.xpath('./li[5]/text()').extract_first()
            item['w_power'] = node.xpath('./li[6]/text()').extract_first()

            # 获取的数据返回给引擎
            yield item

        


        








    