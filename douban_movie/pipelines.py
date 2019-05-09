# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

import json
from scrapy.pipelines.images import ImagesPipeline
from scrapy.exceptions import DropItem
from scrapy import Request
import codecs


class DoubanMoviePipeline(object):
    def open_spider(self,spider):
        self.file = open('double_movie.json','w',encoding='utf-8')

    def process_item(self, item, spider):
        content = json.dumps(dict(item),ensure_ascii=False)+'\n'
        self.file.write(content)
        return item
    def close_spider(self,spider):
        self.file.close()

#下载图片
class DownloadImagesPipeline(ImagesPipeline):
    def get_media_requests(self,item,info):
        for image_url in item['film_image_url']: 
            #添加mate是为了重命名文件使用
            yield Request(image_url,meta={'item':item,'index':item['film_image_url'].index(image_url)})
    
    def file_path(self,request,response=None,info=None):
        item=request.meta.get('item')
        #传递列表中当前下载图片的下标
        index=request.meta.get('index')

        #获得图片名
        image_guid = item['film_name'][index]+'.'+request.url.split('/')[-1].split('.')[-1]

        filename=u'full/{0}'.format(image_guid)
        return filename