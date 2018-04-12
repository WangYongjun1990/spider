# -*- coding:utf-8 -*-
"""
File Name: xianjinbaika
Version:
Description: 检查给定的手机号是否注册了 现金白卡app
Author: wangyongjun
Date: 2018/4/10 16:54
"""

import requests

ua = 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36'

headers = {'User-Agent': ua,
           'Content-Type': 'application/x-www-form-urlencoded; charset=utf-8'}


def if_xianjinbaika(phone, timeout, proxies=None, **kwargs):
    url = 'https://credit.xianjincard.com/credit-user/login-new'

    data = {
        'phone': phone,
        'password': 'jdjdjenne602',
        'type': 1
    }

    """
        请求返回值
        {"code":-1,"message":"用户不存在","data":[]}
        {u'message': u'\u7528\u6237\u4e0d\u5b58\u5728', u'code': -1, u'data': []}
    """

    try:
        res = requests.post(url, data=data, headers=headers, timeout=timeout, proxies=proxies, verify=False)
    except:
        return 3

    try:
        result = res.json().get("message")
    except:
        return 2
    if u"用户不存在" in result:
        return 0
    else:
        return 1

if __name__ == "__main__":
    print if_xianjinbaika('18321248292', 10)
