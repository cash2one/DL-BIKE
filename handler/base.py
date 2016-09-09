# coding=utf-8

import os
import glob
import re

import ujson
import importlib
import time
from tornado import gen, web
from tornado.util import ObjectDict

# 动态创建类,加载全局pageservice方法
obDict = {}
d = os.path.abspath(os.path.join(os.path.dirname(__file__), os.pardir)) + "/service/page/**/*.py"
for module in filter(lambda x: not x.endswith("init__.py"), glob.glob(d)):
    p = module.split("/")[-2]
    m = module.split("/")[-1].split(".")[0]
    m_list = [item.title() for item in re.split(u"_", m)]
    pmPS = "".join(m_list) + "PageService"
    pmObj = m + "_ps"
    obDict.update({
        pmObj: getattr(importlib.import_module('service.page.{0}.{1}'.format(p, m)), pmPS)()
    })

_base = type("_base", (web.RequestHandler,), obDict)

class BaseHandler(_base):

    def __init__(self, application, request, **kwargs):
        super(BaseHandler, self).__init__(application, request, **kwargs)
        self.json_args = None
        self.params = None
        self._log_info = None
        self.start_time = time.time()

        self.city_ps = getattr(importlib.import_module('service.page.{0}.{1}'.format('wechat', 'city')),
                                  'CityPageService')()
        self.scrap_log_ps = getattr(importlib.import_module('service.page.{0}.{1}'.format('wechat', 'scrap_log')),
                                 'ScrapLogPageService')()
        self.station_ps = getattr(importlib.import_module('service.page.{0}.{1}'.format('wechat', 'station')),
                                   'StationPageService')()
        self.user_ps = getattr(importlib.import_module('service.page.{0}.{1}'.format('wechat', 'user')),
                                   'UserPageService')()

    @property
    def logger(self):
        return self.application.logger

    @property
    def settings(self):
        return self.application.settings

    @property
    def constant(self):
        return self.application.constant

    @property
    def log_info(self):
        if self._log_info and dict(self._log_info):
            return self._log_info
        return None

    @log_info.setter
    def log_info(self, value):
        if dict(value):
            self._log_info = dict(value)

    def prepare(self):
        self.json_args = None
        headers = self.request.headers
        try:
            if("application/json" in headers.get("Content-Type", "") and
               self.request.body != ""):
                self.json_args = ujson.loads(self.request.body)
        except Exception as e:
            self.logger.error(e)

    # def get_current_user(self):

    def on_finish(self):
        info = ObjectDict(
            handler=__name__ + '.' + self.__class__.__name__,
            module=self.__class__.__module__.split(".")[1],
            status_code=self.get_status()
        )

        if self.log_info:
            info.update(self.log_info)

        self.logger.record(
            ujson.dumps(self._get_info_header(info), ensure_ascii=0))

    def write_error(self, status_code, **kwargs):

        if status_code == 403:
            self.send_json({
                "msg": u"用户未被授权请求"
            }, status_code=403)
        elif status_code == 404:
            self.send_json({
                "msg": u"资源不存在"
            }, status_code=404)
        else:
            self.send_json({
                "msg": u"服务器错误"
            }, status_code=500)

    def send_json(self, chunk, status_code=200):

        '''
        用于发送含有 objectid 数据类型的数据
        :param chunk:
        :return:

        usage:
            200（请求成功）: Request succeeded for a GET call, for a DELETE or POST call that completed synchronously,
                or for a PUT call that synchronously updated an existing resource
            403（用户未被授权请求） Forbidden: Request failed because user does not have authorization to access a specific resource
            404（资源不存在）Resource not found
            416（参数错误，或不符合业务逻辑的返回）Requested Range Not Satisfiable
            500（服务器错误） Internal Server Error: Something went wrong on the server, check status site and/or report the issue

        reutrn:
            {
                "msg": success or 错误信息
                "data": []
            }
        '''
        if status_code == 200:
            chunk.update({
                "msg": self.constant.RESPONSE_SUCCESS
            })
        self.log_info = {"res_type": "json"}
        self.set_header("Content-Type", "application/json; charset=UTF-8")
        self.set_status(status_code)
        self.write(chunk)
        return

    def _get_info_header(self, log_params):
        request = self.request
        req_params = request.arguments

        log_info_common = ObjectDict(
            elapsed_time="%.4f" % (time.time() - self.start_time),
            useragent=request.headers.get('User-Agent'),
            referer=request.headers.get('Referer'),
            remote_ip=(
                request.headers.get('Remoteip') or
                request.headers.get('X-Forwarded-For') or
                request.remote_ip
            ),
            req_type=request.method,
            req_uri=request.uri,
            req_params=req_params,
        )

        log_params.update(log_info_common)
        return ujson.encode(log_params)