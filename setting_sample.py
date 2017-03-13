# coding=utf-8

'''
说明:
setting配置常量规范：
1.常量适用于整个系统，偏系统设置，如数据库配置、服务器路径等
2.常量不涉及具体业务逻辑（业务逻辑常量配置在constant.py中）
3.尽量考虑复用性
'''
import os
from tornado.options import define

#############################以下内容为系统设置，搭建项目时可根据数据库、redis设置进行调整###############

define("port", default=8016, help="run on the given port", type=int)
define("logpath", default="logs/", help="log path")

settings = {}
settings['xsrf_cookies'] = True
settings['cookie_secret'] = "EAB1D2UT15EEF04D35BA5FDF789DW6B3"
settings['debug'] = True
settings['log_level'] = "DEBUG"

settings['root_path'] = os.path.join(os.path.dirname(__file__), "")
settings['template_path'] = os.path.join(settings['root_path'], "template")
settings['static_path'] = os.path.join(settings['root_path'], "static")
# settings['static_upload_path'] = os.path.join(settings['static_path'], "upload")

settings['static_domain'] = 'http://cdn.hztrip.org'

# 数据库配置
settings['mysql_host'] = "127.0.0.1"
settings['mysql_port'] = 3306
settings['mysql_database'] = "bike"
settings['mysql_user'] = "root"
settings['mysql_password'] = ""

# session配置
settings['store_options'] = {
    'redis_host': '127.0.0.1',
    'redis_port': 6379,
    'redis_pass': '',
    'max_connections': 500
}

settings['proxy'] = "http://127.0.0.1:8016"
settings['baidu_ak'] = "lSbGt6Z31wK9Pwi2GLUCx6ywLeflbjHf"