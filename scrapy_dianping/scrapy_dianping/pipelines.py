# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

import os


class ScrapyDianpingPipeline(object):
    def process_item(self, item, spider):

        save_path = os.path.abspath('.')

        result_file = save_path + '\\results\\' + item['keyword'] + '.txt'

        with open(result_file, "a") as fp:
            fp.write(item['keyword'] + '\t' +
                     item['shop_name'] + '\t' +
                     item['review_num'] + '\t' +
                     item['shop_tag'] + '\t' +
                     item['avg_price'] + '\n')
        return item
