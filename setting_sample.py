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

define("port", default=8080, help="run on the given port", type=int)
define("logpath", default="logs/", help="log path")

settings = {}
settings['xsrf_cookies'] = True
settings['cookie_secret'] = "EAB1D2UT05EEF04D35BA5FDF789DW6B3"
settings['debug'] = True
settings['log_level'] = "DEBUG"

# 数据库配置
settings['mysql_host'] = "127.0.0.1"
settings['mysql_port'] = 3306
settings['mysql_database'] = "bike"
settings['mysql_user'] = "root"
settings['mysql_password'] = ""

# session配置
settings['session_secret'] = "FILUCtuulhrweuflhwesoihqwurwhfbaskldhquwvrlqkwjfv"
settings['session_timeout'] = 3600
settings['store_options'] = {
    'redis_host': '127.0.0.1',
    'redis_port': 6379,
    'redis_pass': ''
}