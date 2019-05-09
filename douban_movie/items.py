# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class DoubanMovieItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    film_name = scrapy.Field()
    film_directors =scrapy.Field()
    film_rate = scrapy.Field()
    film_actors = scrapy.Field()
    film_image_url = scrapy.Field()
    
