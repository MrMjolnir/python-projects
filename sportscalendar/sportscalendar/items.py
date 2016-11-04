# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class scItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
	nombre = scrapy.Field()
	surl  = scrapy.Field()
	sitio = scrapy.Field()
	fecha = scrapy.Field()
#    pass
