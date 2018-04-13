# -*- coding:utf-8 -*-
"""
File Name: log
Version:
Description:
Author: liuxuewen
Date: 2018/1/8 14:23
"""
import logging

logger=logging
logger.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s',
                    datefmt='%a, %d %b %Y %H:%M:%S',
                    filename='myapp.log',
                    filemode='w')

logger.debug('This is debug message')
logger.info('This is info message')
logger.warning('This is warning message')