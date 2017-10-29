# coding=utf-8

# @Time    : 2/6/17 15:24
# @Author  : panda (panyuxin@moseeker.com)
# @File    : metabase.py
# @DES     : 基础 Base，只包含一些公共方法，不涉及到业务逻辑，
#            仅供 BaseHandler 调用，或与 BaseHandler 不同业务逻辑时调用

from tornado import gen

from handler.metabase import MetaBaseHandler
from util.tool.str_tool import to_str
from util.tool.url_tool import url_subtract_query, make_url


class BaseHandler(MetaBaseHandler):

    def __init__(self, application, request, **kwargs):
        super(BaseHandler, self).__init__(application, request, **kwargs)

    @gen.coroutine
    def prepare(self):
        """用于生成 current_user"""

        yield gen.sleep(0.001)  # be nice to cpu

    def make_url(self, path, params=None, host="", protocol="https", escape=None, **kwargs):
        """
        host 环境不能直接从 request 中获取，需要根据环境确定
        :param path:
        :param host:
        :param params:
        :param protocol:
        :param escape:
        :param kwargs:
        :return:
        """
        if not host:
            host = self.host
        return make_url(path, params, host, protocol, escape, **kwargs)

    def fullurl(self, encode=True):
        """
        获取当前 url， 默认删除 query 中的 code 和 state。

        和 oauth 有关的 参数会影响 prepare 方法
        :param encode: False，不会 Encode，主要用在生成 jdsdk signature 时使用
        :return:
        """

        full_url = to_str(self.request.full_url())

        if not self.host in self.request.full_url():
            full_url = full_url.replace(self.settings.m_host, self.host)

        if not encode:
            return full_url
        return url_subtract_query(full_url, ['code', 'state'])
