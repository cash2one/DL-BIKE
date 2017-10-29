# coding=utf-8

# @Time    : 10/27/16 14:35
# @Author  : panda (panyuxin@moseeker.com)
# @File    : hr_wx_rule.py
# @DES     : dataservice的父类
# 负责与DAO交互，实现原子性的操作。一个DAO对应一个dataservice，不能被handler调用，只能被pageservice调用，可被多个pageservice调用
# dataservice之间不能相互调用
# 可以根据表名创建dataservice

import ujson
import glob
import importlib
import re
import random
from tornado import gen

from app import logger, redis
from setting import settings
from util.common import ObjectDict
from util.common.singleton import Singleton
from util.tool.http_tool import http_get
from cache.ipproxy import IpproxyCache


class DataService:
    __metaclass__ = Singleton

    def __init__(self):
        self.logger = logger
        self.redis = redis
        self.ipproxy = IpproxyCache()

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

    @gen.coroutine
    def get_ip_proxy(self):
        """
        获得代理 IP
        referer: https://github.com/qiyeboy/IPProxyPool
        http://121.40.219.23:8100?count=10
        :return:
        """

        ipproxy_session_dict = self.ipproxy.get_ipproxy_session()
        self.logger.debug("ipproxy_session_dict:{}".format(ipproxy_session_dict))
        if ipproxy_session_dict:
            host, value = random.choice(list(ipproxy_session_dict.items()))
            return value['host'], value['port']

        else:

            jdata = ObjectDict({
                'count': 50,  # 数量
                'protocol': 0,  # 0: http, 1 https, 2 http/https
                # 'types': 2, # 0: 高匿,1:匿名,2 透明
            })

            ret = yield http_get(settings['proxy'], jdata)

            res_dict = ObjectDict()
            for item in ret:
                ip_dict = ObjectDict({
                    "host": item[0],
                    "port": item[1],
                })
                res_dict.update({
                    item[0]: ip_dict
                })

            self.ipproxy.set_ipproxy_session(res_dict)

            if res_dict:
                host, value = random.choice(list(res_dict.items()))
                return value['host'], value['port']
            else:
                return "", ""
