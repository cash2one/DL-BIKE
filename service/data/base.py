# coding=utf-8

'''
:author pyx0622@gmail.com
:date 2016.07.26

说明:
dataservice的父类
负责与DAO交互，实现原子性的操作。一个DAO对应一个dataservice，不能被handler调用，只能被pageservice调用，可被多个pageservice调用
dataservice之间不能相互调用
可以根据表名创建dataservice
'''

import importlib

from utils.common.log import Logger
import conf.common as constant


class Singleton(type):

    def __init__(cls, name, bases, dict):
        super(Singleton, cls).__init__(name, bases, dict)
        cls._instance = None

    def __call__(cls, *args, **kw):
        if cls._instance is None:
            cls._instance = super(Singleton, cls).__call__(*args, **kw)
        return cls._instance

class DataService:

    __metaclass__ = Singleton

    def __init__(self):

        self.logger = Logger
        self.constant = constant

        self.city_dao = getattr(importlib.import_module('dao.{0}.{1}'.format('wechat', 'city')),
                                      'CityDao')()
        self.scrap_log_dao = getattr(importlib.import_module('dao.{0}.{1}'.format('wechat', 'scrap_log')),
                                           'ScrapLogDao')()
        self.station_dao = getattr(importlib.import_module('dao.{0}.{1}'.format('wechat', 'station')),
                                        'StationDao')()
        self.user_dao = getattr(importlib.import_module('dao.{0}.{1}'.format('wechat', 'user')),
                                        'UserDao')()
