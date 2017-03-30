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
from util.tool.str_tool import to_str
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
        https://github.com/jhao104/proxy_pool
        http://121.40.219.23:5000/get_all
        :return:
        """

        ipproxy_session_dict = self.ipproxy.get_ipproxy_session()
        if ipproxy_session_dict:
            ip_proxys = list(ipproxy_session_dict.values())
            if len(ip_proxys) > 3:
                ip_proxy = ip_proxys[random.randint(0,2)]
                return ip_proxy.get("host"), ip_proxy.get("port")
            else:
                return "",""
        else:

            ret = yield http_get("{}/{}".format(settings['proxy'], "get_all"), res_json=False)
            res_dict = ObjectDict()
            ret = ujson.decode(to_str(ret))

            for item in ret:
                res_ip = re.split(":", item)
                ip_dict = ObjectDict({
                    "host": res_ip[0],
                    "port": int(res_ip[1])
                })
                res_dict.update({
                    res_ip[0]: ip_dict
                })

            self.ipproxy.set_ipproxy_session(res_dict)

            ip_proxys = list(res_dict.values())
            if len(ip_proxys) > 3:
                ip_proxy = ip_proxys[random.randint(0,2)]
                return ip_proxy.get("host"), ip_proxy.get("port")
            else:
                return "",""

    @gen.coroutine
    def del_ip_proxy(self, ip, port):
        """
        删除代理 IP
        referer: https://github.com/jhao104/proxy_pool
        http://127.0.0.1:5000/delete?proxy=127.0.0.1:8080
        :param ip: 类似192.168.1.1:8080
        :return:
        """

        ipproxy_session_dict = self.ipproxy.get_ipproxy_session()

        if ipproxy_session_dict:
            ipproxy_session_dict.pop(ip, None)
            self.ipproxy.set_ipproxy_session(ipproxy_session_dict)

        params = ObjectDict({
            "proxy": "{}:{}".format(ip, port),
        })

        ret = yield http_get("{}/{}".format(settings['proxy'], "delete"), params, res_json=False)
        raise gen.Return(ret)
