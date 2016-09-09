# -*- coding: utf-8 -*-

"""
api 调用工具类，
"""
import ujson
import tornado.httpclient
from tornado import gen
from tornado.httputil import url_concat, HTTPHeaders
import constant

@gen.coroutine
def http_get(route, jdata=None, headers={}, timeout=5):

    headers.update(constant.COMMON_UA)

    url = url_concat(route, jdata)
    http_client = tornado.httpclient.AsyncHTTPClient()
    response = yield http_client.fetch(
        url,
        request_timeout = timeout,
        method = "GET",
        headers = HTTPHeaders(headers))

    content_type = response.headers.get('Content-Type', '')
    if "application/json" in content_type:
        body = ujson.loads(response.body)
        raise gen.Return(body)

    raise gen.Return(response.body)

@gen.coroutine
def http_post(url, jdata, headers={}, timeout=5):

    headers.update(constant.COMMON_UA)
    print (headers)

    http_client = tornado.httpclient.AsyncHTTPClient()
    response = yield http_client.fetch(
        url,
        method = "POST",
        body = jdata,
        request_timeout = timeout,
        headers = HTTPHeaders(headers)
    )

    content_type = response.headers.get('Content-Type', '')
    if "application/json" in content_type:
        print (23)
        body = ujson.loads(response.body)
        raise gen.Return(body)

    raise gen.Return(response.body)
