# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class ScrapyfItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    title = scrapy.Field()
    date = scrapy.Field()
    link = scrapy.Field()
    content = scrapy.Field()


class LanjiaModel(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    title = scrapy.Field()
    price = scrapy.Field()
    unitPrice = scrapy.Field()
    house = scrapy.Field()
    lever = scrapy.Field()
    area = scrapy.Field()
    label = scrapy.Field()
    areaName = scrapy.Field()
    username = scrapy.Field()
    phone = scrapy.Field()

