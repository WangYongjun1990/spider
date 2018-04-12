# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class ScrapyDianpingItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    # city = scrapy.Field()
    # rank = scrapy.Field()
    # shop_name = scrapy.Field()
    # region = scrapy.Field()
    # score_flavor = scrapy.Field()
    # score_environment = scrapy.Field()
    # score_service = scrapy.Field()
    # avg_price = scrapy.Field()

    keyword = scrapy.Field()
    shop_name = scrapy.Field()
    review_num = scrapy.Field()
    avg_price = scrapy.Field()
    shop_tag = scrapy.Field()

