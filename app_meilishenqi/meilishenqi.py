# -*- coding:utf-8 -*-
"""
File Name: meilishenqi
Version:
Description:
Author: wangyongjun
Date: 2018/4/10 15:00
"""

import requests


def is_register(phone_number):
    url = "https://user.meilimei.com/api/user/login?password=jdjdheuhb&udid=1f8965b4c5c5b2c521949ecc40b21d36&mobile=" + phone_number
    headers = {
        "User-Agent": "meilishenqi/5.5.4.2;android/22;phone/HWATH",
    }

    r = requests.get(url, headers=headers, verify=False)

    print r.status_code
    print r.text
    message = r.json()['message']
    print message, type(message)
    if u'用户不存在' in message:
        print 'not exist'


if __name__ == '__main__':
    is_register('18705141271')
