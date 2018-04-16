# -*- coding:utf-8 -*-

"""
File Name: `test_dianping_top100`.py
Version:
Description: 爬取南京评价最高的100家餐厅信息，对应网页 http://www.dianping.com/shoplist/search/5_10_0_score

Author: wangyongjun
Date: 2018/4/13 11:45
"""

import requests

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.115 Safari/537.36',
}


def dianping_food_top100():
    url = 'http://www.dianping.com/mylist/ajax/shoprank?cityId=5&shopType=10&rankType=score&categoryId=0'

    try:
        r = requests.get(url, headers=headers, timeout=10, proxies=None, verify=False)
        # print r.text
    except Exception as e:
        print e

    shop_list = r.json().get('shopBeans')
    print shop_list
    print type(shop_list), len(shop_list)

    for shop_dict in shop_list:
        print shop_dict['shopName'], shop_dict['score1'], shop_dict['score2'], shop_dict['score3'], shop_dict['avgPrice']


if __name__ == "__main__":
    dianping_food_top100()