# -*- coding: utf-8 -*-

import re
import sys
import scrapy

from bs4 import BeautifulSoup

from scrapy_dianping.items import ScrapyDianpingItem

reload(sys)
sys.setdefaultencoding("utf-8")


class SpiderDianpingFoodSpider(scrapy.Spider):
    name = 'spider_dianping_food'
    # allowed_domains = ['dianping.com']
    # start_urls = ['http://dianping.com/']

    def __init__(self, name=None, **kwargs):
        super(SpiderDianpingFoodSpider, self).__init__(name, **kwargs)
        self.MAX_PAGE_NUMBER = 4

    def start_requests(self):
        """
        生成某城市评价最高的餐厅页面
        :return:
        """
        url_dict = {
            u'雨花客厅美食': r'http://www.dianping.com/search/keyword/5/0_%E9%9B%A8%E8%8A%B1%E5%AE%A2%E5%8E%85%E7%BE%8E%E9%A3%9F',
            u'虹悦城美食': r'https://www.dianping.com/search/keyword/5/0_%E8%99%B9%E6%82%A6%E5%9F%8E%E7%BE%8E%E9%A3%9F',
            u'德基广场美食': 'https://www.dianping.com/search/keyword/5/0_%E5%BE%B7%E5%9F%BA%E5%B9%BF%E5%9C%BA%E7%BE%8E%E9%A3%9F',
        }

        for keyword, url in url_dict.items():
            request = scrapy.Request(url, callback=self.parse)
            request.meta['keyword'] = keyword
            yield request

        # url = r'http://www.dianping.com/search/keyword/5/0_%E9%9B%A8%E8%8A%B1%E5%AE%A2%E5%8E%85%E7%BE%8E%E9%A3%9F'
        # request = scrapy.Request(url, callback=self.parse)
        # yield request

    def parse(self, response):

        keyword = response.meta.get('keyword')

        soup = BeautifulSoup(response.body, "lxml")
        # print soup
        shop_list = soup.find('div', attrs={'id': 'shop-all-list'})
        # print shop_list
        li_list = shop_list.find_all('li')

        for shop in li_list:

            item = ScrapyDianpingItem()

            item['keyword'] = keyword

            try:
                item['shop_name'] = shop.find('h4').string
            except AttributeError:
                item['shop_name'] = 'error'

            try:
                item['review_num'] = shop.find('a', attrs={'class': 'review-num'}).find('b').string
            except AttributeError:
                item['review_num'] = '0'

            try:
                item['avg_price'] = shop.find('a', class_='mean-price').find('b').string
            except AttributeError:
                item['avg_price'] = '-'

            try:
                item['shop_tag'] = shop.find('a', attrs={'data-click-name': 'shop_tag_cate_click'}).find('span').string
            except AttributeError:
                item['shop_tag'] = ''

            # print item['shop_name'], item['review_num'], item['avg_price'], item['shop_tag']
            yield item

        try:
            next_page = soup.find('div', class_='page').find_all('a', class_='next')
        except AttributeError:
            next_page = []
        if next_page:
            next_page_url = next_page[0].get('href')

            pattern = re.compile(r'/p(\d+)')
            page_number = re.findall(pattern, next_page_url)[0]

            if int(page_number) <= self.MAX_PAGE_NUMBER:
                request = scrapy.Request(next_page_url, callback=self.parse)
                request.meta['keyword'] = keyword
                yield request
            else:
                self.logger.info("---over MAX_PAGE_NUMBER {}---".format(self.MAX_PAGE_NUMBER))
