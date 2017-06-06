# coding=utf-8


"""基础服务 api 调用工具"""

import traceback
import ujson
from urllib.parse import urlencode

import tornado.httpclient
from tornado import gen
from tornado.httputil import url_concat

from app import logger
import conf.headers as const_headers
from util.common import ObjectDict


@gen.coroutine
def http_get(
        route,
        jdata=None,
        res_json=True,
        timeout=5,
        proxy_host=None,
        proxy_port=None,
        headers=None):
    ret = yield _async_http_get(route, jdata, res_json, headers, timeout=timeout, proxy_host=proxy_host, proxy_port=proxy_port, method='GET')
    raise gen.Return(ret)


@gen.coroutine
def http_delete(
        route,
        jdata=None,
        res_json=True,
        timeout=5,
        proxy_host=None,
        proxy_port=None,
        headers=None):
    ret = yield _async_http_get(route, jdata, res_json, headers, timeout=timeout, proxy_host=proxy_host, proxy_port=proxy_port, method='DELETE')
    raise gen.Return(ret)


@gen.coroutine
def http_post(
        route,
        jdata=None,
        res_json=True,
        timeout=5,
        proxy_host=None,
        proxy_port=None,
        headers=None):
    ret = yield _async_http_post(route, jdata, res_json, headers, timeout=timeout, proxy_host=proxy_host, proxy_port=proxy_port, method='POST')
    raise gen.Return(ret)


@gen.coroutine
def http_put(
        route,
        jdata=None,
        res_json=True,
        timeout=5,
        proxy_host=None,
        proxy_port=None,
        headers=None):
    ret = yield _async_http_post(route, jdata, res_json, headers, timeout=timeout, proxy_host=proxy_host, proxy_port=proxy_port, method='PUT')
    raise gen.Return(ret)


@gen.coroutine
def http_patch(
        route,
        jdata=None,
        res_json=True,
        timeout=5,
        proxy_host=None,
        proxy_port=None,
        headers=None):
    ret = yield _async_http_post(route, jdata, res_json, headers, timeout=timeout, proxy_host=proxy_host, proxy_port=proxy_port, method='PATCH')
    raise gen.Return(ret)


@gen.coroutine
def http_fetch(
        route,
        data=None,
        res_json=True,
        timeout=5,
        proxy_host=None,
        proxy_port=None,
        headers=None):
    """
    使用 www-form 形式异步请求，支持 GET，POST
    :param route:
    :param jdata:
    :param res_json:
    :param timeout:
    :param headers:
    :return:
    """

    if data is None:
        data = ObjectDict()

    if headers is None:
        headers = const_headers.COMMON_HEADER

    tornado.httpclient.AsyncHTTPClient.configure(
        "tornado.curl_httpclient.CurlAsyncHTTPClient")

    http_client = tornado.httpclient.AsyncHTTPClient()

    try:
        http_request = tornado.httpclient.HTTPRequest(
            route,
            method="POST",
            body=urlencode(data),
            request_timeout=timeout,
            headers=headers,
            validate_cert=False,
            proxy_host=proxy_host,
            proxy_port=proxy_port
        )
        response = yield http_client.fetch(http_request)

        if res_json:
            #  返回结果为 JSON 形式
            # logger.debug("[http_fetch][url: {}][body: {}][ret: {}] ".format(
            #     route, ujson.encode(data), ujson.decode(response.body)))
            body = ujson.decode(response.body)
            raise gen.Return(_objectdictify(body))
        else:
            raise gen.Return(response.body)

    except tornado.httpclient.HTTPError as e:
        logger.warning("[http_fetch][url: {}][body: {}]".format(
            route, ujson.encode(data)))
        logger.warning("http_fetch httperror: {}".format(e))

    raise gen.Return(ObjectDict())


@gen.coroutine
def _async_http_get(
        url,
        jdata=None,
        res_json=True,
        headers=None,
        timeout=5,
        proxy_host=None,
        proxy_port=None,
        method='GET'):
    """可用 HTTP 动词为 GET 和 DELETE"""
    if method.lower() not in "get delete":
        raise ValueError("method is not in GET and DELETE")

    if jdata is None:
        jdata = ObjectDict()

    if headers is None:
        headers = const_headers.COMMON_HEADER

    tornado.httpclient.AsyncHTTPClient.configure(
        "tornado.curl_httpclient.CurlAsyncHTTPClient")

    http_client = tornado.httpclient.AsyncHTTPClient()

    try:
        url = url_concat(url, jdata)
        http_request = tornado.httpclient.HTTPRequest(
            url,
            request_timeout=timeout,
            method=method.upper(),
            headers=headers,
            validate_cert=False,
            proxy_host=proxy_host,
            proxy_port=proxy_port
        )
        response = yield http_client.fetch(http_request)

        if res_json:
            # 返回结果为 JSON 形式
            # logger.debug("[_async_http_get][url: {}][ret: {}] ".format(
            #     url, ujson.decode(response.body)))
            body = ujson.decode(response.body)
            raise gen.Return(_objectdictify(body))
        else:
            # logger.debug("[_async_http_get][url: {}] ".format(url))
            raise gen.Return(response.body)

    except tornado.httpclient.HTTPError as e:
        logger.warning("[_async_http_get][url: {}] ".format(url))
        logger.warning("_async_http_get httperror: {}".format(e))

    raise gen.Return(ObjectDict())


@gen.coroutine
def _async_http_post(
        url,
        jdata=None,
        res_json=True,
        headers=None,
        timeout=5,
        proxy_host=None,
        proxy_port=None,
        method='POST'):
    """可用 HTTP 动词为 POST, PATCH 和 PUT"""
    if method.lower() not in "post put patch":
        raise ValueError("method is not in POST, PUT and PATCH")

    if jdata is None:
        jdata = ObjectDict()

    if headers is None:
        headers = const_headers.COMMON_HEADER

    tornado.httpclient.AsyncHTTPClient.configure(
        "tornado.curl_httpclient.CurlAsyncHTTPClient")

    http_client = tornado.httpclient.AsyncHTTPClient()

    try:
        http_request = tornado.httpclient.HTTPRequest(
            url,
            method=method.upper(),
            # body=ujson.encode(jdata),
            body=ujson.dumps(jdata, ensure_ascii=False).encode('utf-8'),
            request_timeout=timeout,
            headers=headers,
            validate_cert=False,
            proxy_host=proxy_host,
            proxy_port=proxy_port
        )
        response = yield http_client.fetch(http_request)

        if res_json:
            #  返回结果为 JSON 形式
            # logger.debug("[_async_http_post][url: {}][body: {}][ret: {}] ".format(
            #     url, ujson.encode(jdata), ujson.decode(response.body)))
            body = ujson.decode(response.body)
            raise gen.Return(_objectdictify(body))
        else:
            # logger.debug(
            #     "[_async_http_post][url: {}][body: {}] ".format(
            #         url, ujson.encode(jdata)))
            raise gen.Return(response.body)

    except tornado.httpclient.HTTPError as e:
        logger.warning(
            "[_async_http_post][url: {}][body: {}] ".format(
                url, ujson.encode(jdata)))
        logger.warning("_async_http_post httperror: {}".format(e))

    raise gen.Return(ObjectDict())


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
    finally:
        return ret
