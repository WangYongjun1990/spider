# -*- coding:utf-8 -*-

"""
File Name: `run`.py
Version:
Description:

Author: wangyongjun
Date: 2018/4/11 15:44
"""

from scrapy import cmdline

if __name__ == '__main__':

    cmdline.execute("scrapy crawl spider_dianping_food".split())

