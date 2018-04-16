# -*- coding:utf-8 -*-

"""
File Name: `youdao_translate`.py
Version:
Description: 爬取有道翻译接口，破解sign参数加密反爬机制，可解决{"errorCode":50}

Author: wangyongjun
Date: 2018/4/13 15:51
"""

import hashlib
import random
import time
import requests


class Youdao(object):
    def __init__(self, msg):
        self.url = 'http://fanyi.youdao.com/translate_o?smartresult=dict&smartresult=rule'
        self.msg = msg
        self.S = 'fanyideskweb'
        self.D = 'ebSeFb%=XZ%T[KZ)c(sy!'
        self.salt = self.get_salt()
        self.sign = self.get_sign()

    @staticmethod
    def get_salt():
        salt = int(time.time() * 1000) - random.randint(0, 10)
        return str(salt)

    def get_sign(self):
        v = self.S + self.msg + self.salt + self.D
        print v
        return self.get_md5(v)

    @staticmethod
    def get_md5(value):
        m = hashlib.md5()
        m.update(value.encode(encoding='utf8'))
        hash_value = m.hexdigest()
        print hash_value
        return hash_value

    def get_result(self):

        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.115 Safari/537.36',
            'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
            'Referer': 'http://fanyi.youdao.com/',
            'Cookie': 'OUTFOX_SEARCH_USER_ID=741667649@221.226.85.146',
        }

        data = {
            'i': self.msg,
            'from': 'AUTO',
            'to': 'AUTO',
            'smartresult': 'dict',
            'client': self.S,
            'salt': self.salt,    # 1523605724827
            'sign': self.sign,    # fc20e411dbd6a4349ff8ca3c2977e8d5
            'doctype': 'json',
            'version': '2.1',
            'keyfrom': 'fanyi.web',
            'action': 'FY_BY_CLICKBUTTION',
            'typoResult': 'false'
        }

        try:
            r = requests.post(self.url, data=data, headers=headers, timeout=10, proxies=None, verify=False)
            print r.text
        except Exception as e:
            r = None
            print e

        if r:
            try:
                result = r.json().get('translateResult')[0][0].get('tgt')
            except (TypeError, IndexError):
                result = ''

            return result

if __name__ == "__main__":
    youdao = Youdao(u'箱根')
    print youdao.get_result()
