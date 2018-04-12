# -*- coding:utf-8 -*-

"""
File Name: kakadai
Version:
Description: 检查给定的手机号是否注册了 维信卡卡贷app

Author: wangyongjun
Date: 2018/4/10 17:21
"""

import requests

headers = {
    'User-Agent': 'Dalvik/2.1.0 (Linux; U; Android 5.1.1; ATH-AL00 Build/HONORATH-AL00)',
    'Content-Type': 'application/json; charset=utf-8',
}


def if_kakadai(phone, timeout, proxies=None, **kwargs):
    url = 'http://www.kkcredit.cn/ccl/data/ws/rest/app/isregister'

    json = {
        'mobileNo': phone,
        'h_version': '3.4.1.350',
        'h_appType': 'androidmain',
        'h_clientType': 'android'
    }

    """
        res.text 请求返回值
        已注册 {"resCode":"0","resMsg":"操作成功","content":{"operationResult":true,"displayInfo":"该用户已注册"}}
        未注册 {"resCode":"0","resMsg":"操作成功","content":{"operationResult":false,"displayInfo":"该用户未注册!"}}
    """

    try:
        res = requests.post(url, json=json, headers=headers, timeout=timeout, proxies=proxies, verify=False)
        print res.text
    except:
        return 3

    try:
        result = res.json().get("content").get("operationResult")
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
    # 0 --- 未注册
    # 1 --- 已注册
    # 2 --- 网站返回数据变更
    # 3 --- 网络问题

    # 已注册
    print if_kakadai('13720257610', 10)

    # 未注册
    print if_kakadai('13720257611', 10)
