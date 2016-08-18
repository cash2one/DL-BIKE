# coding=utf-8

'''
:author pyx0622@gmail.com
:date 2016.08.13
:table city

'''

from dao.base import BaseDao

class CityDao(BaseDao):

    def __init__(self):
        super(CityDao, self).__init__()
        self.table = "city"
        self.fields_map = {
            "id": self.constant.TYPE_INT,
            "code": self.constant.TYPE_INT, # 城市code
            "name": self.constant.TYPE_STRING, # 城市中文名
            "ename": self.constant.TYPE_STRING, # 城市英文名
            "level": self.constant.TYPE_INT, # 城市等级
            "is_hot": self.constant.TYPE_INT, # 是否热门城市 0：否 1：是
            "is_using": self.constant.TYPE_INT, # 是否正在使用 0：否 1：是
        }