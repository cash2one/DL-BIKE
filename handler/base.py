# coding=utf-8

import ujson

import tornado.web
from tornado.util import ObjectDict

from utils.tool.json_tool import JSONEncoder
from utils.common.session import Session


class BaseHandler(tornado.web.RequestHandler):

    # Initialization and properties
    def __init__(self, application, request, **kwargs):
        super(BaseHandler, self).__init__(application, request, **kwargs)
        self.json_args = None
        self.params = None
        self._log_info = None

        self.session = Session(self.application.session_manager, self, 1)
        self.session.save()

        # 日志变量
        # pageservice实例化

    @property
    def logger(self):
        return self.application.logger

    @property
    def settings(self):
        return self.application.settings

    @property
    def log_info(self):
        if self._log_info and dict(self._log_info):
            return self._log_info
        return None

    @log_info.setter
    def log_info(self, value):
        if dict(value):
            self._log_info = dict(value)

    # Public API
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

    def guarantee(self, fields_mapping, *args):

        '''
        :param fields_mapping 校验类型。会过滤HTML标签
        usage:
            对输入参数做检查，主要用于post、put

            try:
                self.guarantee("mobile", "name", "password")
            except AttributeError:
                return

            mobile = self.params["mobile"]
        '''

        self.params = {}
        for arg in args:
            try:
                self.params[arg] = self.json_args[arg]
                self.json_args.pop(arg)
            except KeyError:
                ret_field = fields_mapping.get(arg, arg)
                raise AttributeError(u"{0}不能为空".format(ret_field))
            self.params.update(self.json_args)

        return self.params

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

    def add_log(self, log={}):

        '''
        手动添加日志字段
        :return:
        '''
        self._log_info.update(log)

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

        self.log_info = {"res_type": "json"}
        chunk = JSONEncoder().encode(chunk)
        self.set_header("Content-Type", "application/json; charset=UTF-8")
        self.set_status(status_code)
        self.write(chunk)
        return

    # priviate methods
    def _get_info_header(self, log_params):
        request = self.request
        req_params = request.arguments

        log_info_common = ObjectDict(
            useragent=request.headers.get('User-Agent'),
            referer=request.headers.get('Referer'),
            remote_ip=(
                request.headers.get('Remoteip') or
                request.headers.get('X-Forwarded-For') or
                request.remote_ip
            ),
            req_type=request.method,
            req_uri=request.uri,
            session_id=self.get_secure_cookie('session_id'),
        )

        log_info_common.update(req_params)
        log_params.update(log_info_common)

        return JSONEncoder().encode(log_params)
