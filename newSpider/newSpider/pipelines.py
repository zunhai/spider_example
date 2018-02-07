# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html


from newSpider import settings
from scrapy import Request
import requests
import os
from newSpider import trans



class NewspiderPipeline(object):
    def process_item(self, item, spider):
        return item


class MyPipelineForTxt(object):

    def process_item(self, item, spider):
        newTxt = ""
        if 'txt' in item:
            dir_path = 'F:\小说\超级卡牌系统'
            if not os.path.exists(dir_path):
                os.makedirs(dir_path)
            

            txt_file_name = item["zhangjie_name"]
            if len(txt_file_name.split()) == 2:
                file_name1 = txt_file_name.split()[0]
                file_name2 = txt_file_name.split()[1]
            else:
                file_name1 = txt_file_name
                file_name2 = ""
            file_name1 = trans.changeChineseNumToArab(file_name1)
            file_path = '%s\%s %s.txt' % (dir_path, file_name1 , file_name2)
            file_path = file_path.replace("?" , "")
            txt = item["txt"]
                
            newTxt = newTxt.join(txt)
            handle = open(file_path , "w+" , encoding='utf-8')
            handle.write(newTxt)
            handle.close()
                
        return item