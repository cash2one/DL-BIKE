# coding=utf-8
#
# :author pyx0622@gmail.com
# :date 2016.08.13
# :table city

from dao.base import BaseDao

class CityDao(BaseDao):

    def __init__(self):
        super(CityDao, self).__init__()
        self.table = "city"
        self.fields_map = {
            "cid":          self.constant.TYPE_INT, # 城市编码
            "initial":      self.constant.TYPE_STRING, # 首字母
            "pid":          self.constant.TYPE_INT, # 城市所属州（省）
            "pname":        self.constant.TYPE_STRING, # 州（省）的名称
            "cname":        self.constant.TYPE_STRING, # 城市名称
        }

