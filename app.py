# coding=utf-8

'''
系统应用入口 app.py

说明
------------------
* 应用参数初始化
* 应用代理配置
* 启动应用服务

启动系统方式
------------------

shell commond::

    python `pwd`/app.py --port=xxxx --logpath=/path/logs/ &

点我访问 `Moseeker`_.

.. _moseeker: http://localhost:8000
'''

import tornado.httpserver
import tornado.web
import tornado.ioloop
from tornado.options import options

from setting import settings
from route import routes
from util.common.log import MessageLogger
from util.common.cache import BaseRedis

tornado.options.parse_command_line()
logger = MessageLogger(logpath=options.logpath)
redis = BaseRedis()

class Application(tornado.web.Application):

    def __init__(self):
        tornado.web.Application.__init__(self, routes, **settings)

        self.settings = settings
        self.logger = logger
        self.redis = redis

def main():

    application = Application()
    try:
        logger.info('Server starting, on port : {0}'.format(options.port))
        http_server = tornado.httpserver.HTTPServer(application, xheaders=True)
        http_server.listen(options.port)
        tornado.ioloop.IOLoop.instance().start()
    except Exception as e:
        logger.error(e)
    finally:
        logger.info('Server closing, on port : {0}'.format(options.port))

if __name__ == "__main__":
    main()
