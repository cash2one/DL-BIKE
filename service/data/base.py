# coding=utf-8

# @Time    : 10/27/16 14:35
# @Author  : panda (panyuxin@moseeker.com)
# @File    : hr_wx_rule.py
# @DES     : dataservice的父类
# 负责与DAO交互，实现原子性的操作。一个DAO对应一个dataservice，不能被handler调用，只能被pageservice调用，可被多个pageservice调用
# dataservice之间不能相互调用
# 可以根据表名创建dataservice


import glob
import importlib
import re

from app import logger
from setting import settings
from util.common.singleton import Singleton


class DataService:

    __metaclass__ = Singleton

    def __init__(self):
        self.logger = logger

        for module in self._search_path():
            p = module.split("/")[-2]
            m = module.split("/")[-1].split(".")[0]
            m_list = [item.title() for item in re.split("_", m)]
            pm_dao = "".join(m_list) + "Dao"
            pm_obj = m + "_dao"
            klass = getattr(
                importlib.import_module('dao.{0}.{1}'.format(p, m)), pm_dao)
            instance = klass()

            setattr(self, pm_obj, instance)

    @staticmethod
    def _valid_conds(conds):
        ret = False
        if not conds:
            return ret
        return isinstance(conds, dict) or isinstance(conds, str)

    @staticmethod
    def _search_path():
        d = settings['root_path'] + "dao/**/*.py"
        return filter(lambda x: not x.endswith("init__.py"), glob.glob(d))
