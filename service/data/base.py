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

import re
import importlib
import glob

import constant
from utils.common.log import Logger
from setting import settings
from utils.cache import cache
from utils.common.singleton import Singleton


class DataService:

    __metaclass__ = Singleton

    def __init__(self):

        self.logger = Logger
        self.constant = constant

        d = settings['root_path'] + "dao/**/*.py"
        for module in filter(lambda x: not x.endswith("init__.py"), glob.glob(d)):
            p = module.split("/")[-2]
            m = module.split("/")[-1].split(".")[0]
            m_list = [item.title() for item in re.split(u"_", m)]
            pmDao = "".join(m_list) + "Dao"
            pmObj = m + "_dao"

            setattr(self, pmObj, getattr(importlib.import_module('dao.{0}.{1}'.format(p, m)), pmDao)())
