# coding=utf-8

# Copyright 2016 MoSeeker

"""基础服务 api 调用工具"""

import traceback
import tornado.httpclient
import ujson
from tornado import gen
from tornado.httputil import url_concat

from app import logger
import conf.headers as const_headers
from util.common import ObjectDict

@gen.coroutine
def http_get(route, jdata=None, res_json=True, timeout=5, headers=None):
    ret = yield _async_http_get(route, jdata, res_json, headers, timeout=timeout, method='GET')
    raise gen.Return(ret)


@gen.coroutine
def http_delete(route, jdata=None, res_json=True, timeout=5, headers=None):
    ret = yield _async_http_get(route, jdata, res_json, headers, timeout=timeout, method='DELETE')
    raise gen.Return(ret)


@gen.coroutine
def http_post(route, jdata=None, res_json=True, timeout=5, headers=None):
    ret = yield _async_http_post(route, jdata, res_json, headers, timeout=timeout, method='POST')
    raise gen.Return(ret)


@gen.coroutine
def http_put(route, jdata=None, res_json=True, timeout=5, headers=None):
    ret = yield _async_http_post(route, jdata, res_json, headers, timeout=timeout, method='PUT')
    raise gen.Return(ret)


@gen.coroutine
def http_patch(route, jdata=None, res_json=True, timeout=5, headers=None):
    ret = yield _async_http_post(route, jdata, res_json, headers, timeout=timeout, method='PATCH')
    raise gen.Return(ret)


def _objectdictify(result):
    """将结果 ObjectDict 化"""
    ret = result
    try:
        if isinstance(result, list):
            ret = [ObjectDict(e) for e in result]
        elif isinstance(result, dict):
            ret = ObjectDict(result)
        else:
            pass
    except Exception as e:
        logger.error(traceback.format_exc())
        pass
    finally:
        return ret


@gen.coroutine
def _async_http_get(url, jdata=None, res_json=True, headers=None, timeout=5, method='GET'):
    """可用 HTTP 动词为 GET 和 DELETE"""
    if method.lower() not in "get delete":
        raise ValueError("method is not in GET and DELETE")

    if jdata is None:
        jdata = ObjectDict()

    if headers is None:
        headers = const_headers.COMMON_UA

    url = url_concat(url, jdata)
    http_client = tornado.httpclient.AsyncHTTPClient()
    response = yield http_client.fetch(
        url,
        request_timeout=timeout,
        method=method.upper(),
        headers=headers,
    )

    if res_json:
        # 返回结果为 JSON 形式
        logger.debug("[_async_http_get][url: {}][ret: {}] ".format(
            url, ujson.decode(response.body)))
        body = ujson.decode(response.body)
        raise gen.Return(_objectdictify(body))
    else:
        raise gen.Return(response.body)


@gen.coroutine
def _async_http_post(url, jdata=None, res_json=True, headers=None, timeout=5, method='POST'):
    """可用 HTTP 动词为 POST, PATCH 和 PUT"""
    if method.lower() not in "post put patch":
        raise ValueError("method is not in POST, PUT and PATCH")

    if jdata is None:
        jdata = ObjectDict()

    if headers is None:
        headers = const_headers.COMMON_UA

    http_client = tornado.httpclient.AsyncHTTPClient()
    response = yield http_client.fetch(
        url,
        method=method.upper(),
        body=ujson.encode(jdata),
        request_timeout=timeout,
        headers=headers,
    )
    # headers = HTTPHeaders({"Content-Type": "application/json"}

    if res_json:
        #  返回结果为 JSON 形式
        logger.debug("[_async_http_post][url: {}][body: {}][ret: {}] ".format(
            url, ujson.encode(jdata), ujson.decode(response.body)))
        body = ujson.decode(response.body)
        raise gen.Return(_objectdictify(body))
    else:
        raise gen.Return(response.body)