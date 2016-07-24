# -*- coding: utf-8 -*-

'''
说明:
setting配置常量规范：
1.常量适用于整个系统，偏系统设置，如数据库配置、服务器路径等
2.常量不涉及具体业务逻辑（业务逻辑常量配置在constant.py中）
3.尽量考虑复用性
'''

from tornado.options import define

#############################以下内容为系统设置，搭建项目时可根据数据库、redis设置进行调整###############

define("port", default=8000, help="run on the given port", type=int)
define("logpath", default="logs/", help="log path")

settings = {}
settings['xsrf_cookies'] = True
settings['cookie_secret'] = "EAB1D2AB05EEF04D35BA5FDF789DD6A3"
settings['debug'] = False
settings['log_level'] = "DEBUG"

# 数据库配置 dqv4
settings['mysql_host'] = "qx.dqprism.com"
settings['mysql_port'] = 3306
settings['mysql_database'] = "dqv4"
settings['mysql_user'] = "daqi"
settings['mysql_password'] = "5F51692091B4031640E18E7C27430E071BC878C8"

# session配置
settings['session'] = True
settings['session_secret'] = "FILUCyiulhrweuflhwesoihqwurihfbaskjdhquwvrlqkwjfv"
settings['session_timeout'] = 600
settings['store_options'] = {
    'redis_host': '182.92.131.142',
    'redis_port': 6379,
    'redis_pass': ''
}