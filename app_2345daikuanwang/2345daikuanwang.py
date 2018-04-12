# -*- coding:utf-8 -*-
"""
File Name: 2345daikuanwang
Version:
Description: 检查给定的手机号是否注册了 2345贷款王app
Author: wangyongjun
Date: 2018/4/10 17:34
"""

import requests

ua = 'Loan/5.13.0(os:android)-869372028912494'

headers = {'User-Agent': ua,
           # 'channel': '1034',
           # 'Authorization': 'Basic c3VpeGluZGFpOjFxYXohQCMk',
           'X-DeviceNo': '869372028912494',
           'os': 'android',
           # 'productId': '-1',
           # 'X-Lat': '31.971656',
           'version': '5.13.0',
           # 'X-DeviceToken': '869372028912494',
           # 'X-Ip': '192.168.1.101',
           # 'app-bundle-id': 'com.hyron.b2b2p',
           'Content-Type': 'application/x-www-form-urlencoded',
}


def if_wsdaikuan2345(phone, timeout, proxies=None, **kwargs):
    url = 'https://wsdaikuan.2345.com/b2b2p-ws/api/v5_9_1/isRegistered?version=5.13.0&scene=0220'

    data = {
        'phone': phone
    }

    """
        res.text 请求返回值
        已注册 {"result":{"inWhiteList":false,"registered":true},"error":null}
        未注册 {"result":{"inWhiteList":false,"registered":false},"error":null}
    """

    try:
        res = requests.post(url, data=data, headers=headers, timeout=timeout, proxies=proxies, verify=False)
    except:
        return 3

    try:
        result = res.json().get("result").get("registered")
    except:
        return 2

    if isinstance(result, bool):
        if result:
            return 1
        else:
            return 0
    else:
        return 2

if __name__ == "__main__":
    print if_wsdaikuan2345('13720257610', 10)
    print if_wsdaikuan2345('13720257611', 10)
