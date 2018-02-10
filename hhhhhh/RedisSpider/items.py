# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class RedisspiderItem(scrapy.Item):
    # define the fields for your item here like:
    # 城市，月份，日期，最高气温，最低气温，天气，风向，风力
    # 城市
    city = scrapy.Field()
    # 城市url
    city_url = scrapy.Field()
    # 月份
    month = scrapy.Field()
    # 月份url
    month_url = scrapy.Field()
    # 日期
    date = scrapy.Field()
    # 最高气温
    high_tem = scrapy.Field()
    # 最低气温
    low_tem = scrapy.Field()
    # 天气
    weather = scrapy.Field()
    # 风向
    w_direc = scrapy.Field()
    # 风力
    w_power = scrapy.Field()