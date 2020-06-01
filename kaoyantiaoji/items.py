# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class KaoyantiaojiItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass
    provinceName = scrapy.Field()
    universityName = scrapy.Field()
    majorName = scrapy.Field()
    publishDate = scrapy.Field()
    learnStyle = scrapy.Field()
    articleId = scrapy.Field()
    favorite = scrapy.Field()
    subscribeUniversity = scrapy.Field()
    title = scrapy.Field()
    content = scrapy.Field()
    isNew = scrapy.Field()

