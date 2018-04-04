# -*- coding: utf-8 -*-
import sys
import scrapy
from bs4 import BeautifulSoup

from spider_cydtest.items import SpiderCydtestItem

reload(sys)
sys.setdefaultencoding("utf-8")


class CydtestSpider(scrapy.Spider):
    name = 'cydtest'
    # allowed_domains = ['www.cydtest.com']
    # start_urls = ['http://www.cydtest.com/']

    def __init__(self, name=None, **kwargs):
        super(CydtestSpider, self).__init__(name, **kwargs)
        self.max_pn = 5

    def start_requests(self):
        """
        生成首页列表页
        :return:
        """
        url = r'http://www.cydtest.com/'
        request = scrapy.Request(url, callback=self.parse_list)
        yield request

    def parse_list(self, response):
        # item = SpiderCydtestItem()
        soup = BeautifulSoup(response.body, "lxml")
        # article_title_list = [ele.find('a').string for ele in soup.find_all('h2', class_='entry-title')]
        #
        # for article_title in article_title_list:
        #     item['title'] = article_title
        #     yield item

        article_url_list = [ele.find('a').get('href') for ele in soup.find_all('h2', class_='entry-title')]
        for article_url in article_url_list:
            request = scrapy.Request(article_url, callback=self.parse_article)
            yield request

        next_page = soup.find_all('div', class_='nav-previous')
        if next_page:
            next_page_url = next_page[0].find('a').get('href')
            request = scrapy.Request(next_page_url, callback=self.parse_list)
            yield request

    def parse_article(self, response):
        item = SpiderCydtestItem()
        soup = BeautifulSoup(response.body, "lxml")

        item['title'] = soup.find('h1', class_='entry-title').string

        published_time = soup.find('time', class_='entry-date published')
        updated_time = soup.find('time', class_='entry-date published updated')
        if published_time:
            item['post_time'] = published_time.string  # 换datetime？
        elif updated_time:
            item['post_time'] = updated_time.string
        else:
            item['post_time'] = ''

        category_list = soup.find_all('a', attrs={'rel': 'category'})
        category_all = ''
        for category in category_list:
            category_all += category.string + ','
        item['category'] = category_all

        yield item


