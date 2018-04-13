# -*- coding:utf-8 -*-
"""
File Name: proxies
Version:
Description:
Author: liuxuewen
Date: 2018/1/4 10:06
"""
import itertools
import random
import time
import requests


def get_aws_proxies():
    """
    随机返回一个*aws*代理ip(aws ec2上squid设置) 适用于对爬取质量要求高的网站
    :return:
    """

    ip_list_1 = ['54.222.232.0', '54.222.198.175', '54.222.248.157', '54.222.206.125',
                 '54.222.234.209', '54.223.161.39', '54.223.156.59', '54.223.159.148',
                 '54.223.21.123', '54.222.168.162', '54.223.33.4', '54.223.94.4',
                 ]

    ip_list_2 = ['52.80.79.173', '54.222.203.11', '54.222.205.72', '52.80.83.243',
                 '54.222.241.163', '52.80.11.103', '52.80.28.179', '52.80.34.136',
                 '54.223.198.168', '52.80.44.176', '52.80.45.166', '52.80.38.37'
                 ]

    ip_list_3 = ['52.80.61.73', '52.80.40.255', '52.80.41.23', '52.80.52.24',
                 '52.80.88.180', '52.80.26.246', '52.80.73.35', '52.80.89.0']

    http_str = 'http://{}:3128'

    https_str = 'https://{}:3128'

    proxies_list = [dict(http=http_str.format(ip), https=https_str.format(ip))
                    for ip in itertools.chain(ip_list_1, ip_list_2, ip_list_3)]

    return random.choice(proxies_list)


def get_user_agent():
    useragent_list = [
        'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/535.1 (KHTML, like Gecko) Chrome/14.0.835.163 Safari/535.1',
        'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:6.0) Gecko/20100101 Firefox/6.0',
        'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/534.50 (KHTML, like Gecko) Version/5.1 Safari/534.50',
        'Mozilla/5.0 (Windows; U; Windows NT 6.1; ) AppleWebKit/534.12 (KHTML, like Gecko) Maxthon/3.0 Safari/534.12',
        'Mozilla/5.0 (Windows; U; Windows NT 5.2) AppleWebKit/525.13 (KHTML, like Gecko) Chrome/0.2.149.27 Safari/525.13 ',
        'Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_6_8; en-us) AppleWebKit/534.50 (KHTML, like Gecko) Version/5.1 Safari/534.50',
        'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1)',
        'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; Trident/4.0; SE 2.X MetaSr 1.0; SE 2.X MetaSr 1.0; .NET CLR 2.0.50727; SE 2.X MetaSr 1.0)',
        'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; 360SE)'
        'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.62 Safari/537.36'
    ]
    return random.choice(useragent_list)


def request_get(url):
    headers = dict()
    headers['User-Agent'] = get_user_agent()
    for i in range(5):
        try:
            time.sleep(0.1)
            res = requests.get(url, headers=headers, proxies=get_aws_proxies(), timeout=10)
            return res
        except Exception as e:
            pass
    return None


if __name__ == '__main__':
    for i in range(100):
        res = request_get(
            'https://www.baidu.com/')
        if res:
            print(res.status_code)
