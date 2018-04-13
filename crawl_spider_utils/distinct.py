# -*- coding:utf-8 -*-
"""
File Name: distinct
Version:
Description:
Author: liuxuewen
Date: 2018/1/4 10:56
"""
import sys
import hashlib
import os
import codecs

import redis


"""
利用redis的集合不允许添加重复元素来进行去重
"""







# redis
pool = redis.ConnectionPool(host='99.48.58.244', port=6379, db=10, password='mime@123')
# r = redis.Redis(connection_pool=pool)
r = redis.StrictRedis(connection_pool=pool)




def encrypt_md5(x):
    m = hashlib.md5()
    m.update(x.encode(encoding='utf8'))
    hash_value = m.hexdigest()
    return hash_value


def rem_redis(r,check_str,set_name):
    hash_value = encrypt_md5(check_str)
    r.srem(set_name,hash_value)



def add_redis(r, check_str, set_name):
    """
    将check_str加入redis连接r的set_name集合中
    :param r:redis连接
    :param check_str:被添加的字符串
    :param set_name:项目所使用的集合名称，建议如下格式：”projectname:task_remove_repeate“
    :return:
    """
    hash_value = encrypt_md5(check_str)
    r.sadd(set_name, hash_value)

def is_new(r, check_str, set_name):
    """
    check_str是否为set_name的新元素 新元素返回1 重复元素返回0
    :param r:
    :param check_str:
    :param set_name:
    :return:
    """
    hash_value = encrypt_md5(check_str)
    return 0 if r.sismember(set_name, hash_value) else 1

def redis_close(pool):
    """
    释放redis连接池
    :param pool:
    :return:
    """
    pool.disconnect()

if __name__ == '__main__':
    pass