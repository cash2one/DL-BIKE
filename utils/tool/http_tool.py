# -*- coding: utf-8 -*-

"""
HTTP调用工具类
"""

import ujson

import tornado.httpclient
from tornado import gen
from tornado.httputil import url_concat, HTTPHeaders


@gen.coroutine
def async_http_get(route, jdata, timeout=5):
    """
    适合V2的接口返回，如果数据正确，直接返回data数据，业务方不需要再解析response结构
    """
    url = url_concat(route, jdata)

    http_client = tornado.httpclient.AsyncHTTPClient()

    response = yield http_client.fetch(
        url, request_timeout=timeout,
        headers=HTTPHeaders({"Content-Type": "application/json"}))

    body = ujson.loads(response.body)
    content_type = response.headers.get('Content-Type', '')

    if body.get('status') == 0 and "application/json" in content_type:
        raise gen.Return(body.get('data'))
    raise gen.Return(body)


@gen.coroutine
def async_http_post_v2(route, jdata, timeout=5, method='POST'):
    """
    适合V2的接口返回，如果数据正确，直接返回data数据，业务方不需要再解析response结构
    method 默认为 POST, 但是也可以用其他的 HTTP 方法
    不要使用 GET, 以及其它非 HTTP 动词
    """
    if method.lower() not in "post put delete patch":
        raise ValueError("{method} is not a valid HTTP verb".format(
            method.lower()))

    http_client = tornado.httpclient.AsyncHTTPClient()

    response = yield http_client.fetch(
        route,
        method=method.upper(),
        body=ujson.dumps(jdata),
        request_timeout=timeout,
        headers=HTTPHeaders({"Content-Type": "application/json"})
    )

    body = ujson.loads(response.body)
    content_type = response.headers.get('Content-Type', '')

    if body.get('status', 1) == 0 and "application/json" in content_type:
        raise gen.Return(body.get('data'))
    raise gen.Return(body)
