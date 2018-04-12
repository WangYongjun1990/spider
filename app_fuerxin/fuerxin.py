# -*- coding:utf-8 -*-
"""
File Name: fuerxin
Version:
Description: 富而信app，号码识别是否已注册
Author: wangyongjun
Date: 2018/4/10 14:20
"""

import requests
import json


def is_register(phone_number):
    url = "https://passport.crfchina.com/auth_server/auth/login/" + phone_number
    headers = {
        "User-Agent": "CRF_app/Android/China_Rapid_Finance_3.10.3(Linux; U; Android 5.1.1; ATH-AL00 Build/HONORATH-AL00)",
        "content-type": "application/json; charset=UTF-8",
    }

    json_param = {
        "password": "dfgyyf665",
        "account": phone_number,
    }

    # 开charles代理时，需要加上verify=False
    r = requests.post(url, json=json_param, headers=headers, verify=False)
    # r = requests.post(url, data=json.dumps(json_param), headers=headers, verify=False)

    print r.status_code
    print r.text
    message = r.json()['message']
    print message
    if u'不存在' in message:
        print 'not exist'


if __name__ == '__main__':
    is_register('18705141271')
