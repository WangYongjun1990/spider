# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html


class SpiderCydtestPipeline(object):
    def process_item(self, item, spider):
        with open(r"E:\spider\spider_cydtest\articles.txt", "a") as fp:
            fp.write(item['title'] + '\t' + item['post_time'] + '\t' + item['category'] + '\n')
        return item
