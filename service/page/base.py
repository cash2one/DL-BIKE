# coding=utf-8

'''
:author pyx0622@gmail.com
:date 2016.07.22

说明:
pageservice的父类
负责与handler交互，不能直接与DAO交互。一个pageservice能调用多个dataservice，pageservice只能被handler调用
pageservice之间可以相互调用，但不建议
可以根据业务类型创建pageservice
'''

import importlib

from utils.common.log import Logger
from setting import settings
import conf.common as constant


class Singleton(type):

    def __init__(cls, name, bases, dict):
        super(Singleton, cls).__init__(name, bases, dict)
        cls._instance = None

    def __call__(cls, *args, **kw):
        if cls._instance is None:
            cls._instance = super(Singleton, cls).__call__(*args, **kw)
        return cls._instance

class PageService:

    __metaclass__ = Singleton

    def __init__(self):

        '''
        初始化dataservice
        :return:
        '''
        self.logger = Logger
        self.settings = settings
        self.constant = constant

        self.city_ds = getattr(importlib.import_module('service.data.{0}.{1}'.format('wechat', 'city')),
                                     'CityDataService')()
        self.scrap_log_ds = getattr(importlib.import_module('service.data.{0}.{1}'.format('wechat', 'scrap_log')),
                                          'ScrapLogDataService')()
        self.station_ds = getattr(importlib.import_module('service.data.{0}.{1}'.format('wechat', 'station')),
                                       'StationDataService')()
        self.user_ds = getattr(importlib.import_module('service.data.{0}.{1}'.format('wechat', 'user')),
                                       'UserDataService')()
