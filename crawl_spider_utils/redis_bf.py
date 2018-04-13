# -*- coding:utf-8 -*-
"""
File Name: redis_bf
Version:
Description:
Author: liuxuewen
Date: 2017/5/19 10:37
"""
import redis
from hashlib import sha1


class SimpleHash(object):
    def __init__(self, cap, seed):
        self.cap = cap
        self.seed = seed

    def hash(self, value):
        ret = 0
        for i in range(len(value)):
            ret += self.seed * ret + ord(value[i])

        return (self.cap - 1) & ret


class BloomFilter(object):
    def __init__(self, block_num=1, key="bf"):
        """
        :param block_num: 1 for 90000000
        :param key: key name in redis
        """
        self.r_pool = redis.Redis(host='99.48.58.244', port=6379, db=2, password='mime@123')
        self.bit_size = 1 << 31
        self.seeds = [5, 7, 11, 13, 31, 37, 61]
        self.key = key
        self.block_num = block_num
        self.hash_funcs = [SimpleHash(self.bit_size, seed) for seed in self.seeds]

    def check_in(self, string):
        s1 = sha1()
        s1.update(string)
        s1_res = s1.hexdigest()

        ret = True
        name = self.key + str(int(s1_res[:2], 16) % self.block_num)
        for f in self.hash_funcs:
            loc = f.hash(s1_res)
            ret = ret & self.r_pool.getbit(name, loc)

        return ret

    def insert(self, string):
        s1 = sha1()
        s1.update(string)
        s1_res = s1.hexdigest()

        name = self.key + str(int(s1_res[0:2], 16) % self.block_num)
        for f in self.hash_funcs:
            loc = f.hash(s1_res)
            self.r_pool.setbit(name, loc, 1)


if __name__ == '__main__':
    bf = BloomFilter()
    if bf.check_in('hello, world'):
        print True
    else:
        print False
        bf.insert('hello, world')

    print bf.check_in('hello, world')