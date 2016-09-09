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
import re
import importlib
import glob

from utils.common.log import Logger
from setting import settings
import constant
from utils.common.singleton import Singleton


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

        d = settings['root_path'] + "/service/data/**/*.py"
        for module in filter(lambda x: not x.endswith("init__.py"), glob.glob(d)):
            p = module.split("/")[-2]
            m = module.split("/")[-1].split(".")[0]
            m_list = [item.title() for item in re.split(u"_", m)]
            pmDS = "".join(m_list) + "DataService"
            pmObj = m + "_ds"

            setattr(self, pmObj, getattr(importlib.import_module('service.data.{0}.{1}'.format(p, m)), pmDS)())
