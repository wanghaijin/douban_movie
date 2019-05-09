# -*- coding: utf-8 -*-
import scrapy
import json
import os,stat
import urllib.request
from douban_movie.items import DoubanMovieItem


class FilmReviewSpider(scrapy.Spider):
    name = 'film_review'
    # allowed_domains = ['movie.douban.com']
    start_urls = ['https://movie.douban.com/j/new_search_subjects?sort=U&range=0,10&tags=1&start=0']

    #设置网址偏移量
    offset = 0
    file_path='D:\scrapyK\douban_movie\douban_movie\photos'

    def parse(self, response):
        item = DoubanMovieItem()
        film_list = json.loads(response.body.decode())
        if film_list == [] or self.offset >1000:
            return 
        for film in film_list['data']:
            item['film_name']=film['title']
            item['film_directors']=film['directors']
            item['film_rate']=film['rate']
            item['film_actors']=film['casts']
            item['film_image_url']=film['cover']
            urllib.request.urlretrieve(item['film_image_url'],self.file_path+"/"+item['film_name']+"."+item['film_image_url'].split(".")[-1])
            yield item
        self.offset=self.offset+20
        new_url = 'https://movie.douban.com/j/new_search_subjects?sort=U&range=0,10&tags=1&start='+str(self.offset)
        yield scrapy.Request(url = new_url,callback=self.parse)

        
        