# -*- coding: utf-8 -*-

import functools

from tornado import gen
from tornado.util import ObjectDict

import conf.common as constant


def handle_error(method):

    @functools.wraps(method)
    @gen.coroutine
    def wrapper(self, *args, **kwargs):

        try:
            yield method(self, *args, **kwargs)
        except Exception as e:
            self.logger.error(e)
            self.write_error(500)

    return wrapper

# def url_valid(func):
#
#     '''
#     # TODO 功能待调整
#     :param func:
#     :return:
#     '''
#
#     @functools.wraps(func)
#     @gen.coroutine
#     def wrapper(self, *args, **kwargs):
#
#         try:
#             if not getattr(self, "_current_user", None):
#                 self._current_user = yield self.get_current_user()
#                 self._current_user = ObjectDict(self._current_user)
#             yield func(self, *args, **kwargs)
#
#         except Exception, e:
#             self.logger.error(e)
#             return
#     return wrapper