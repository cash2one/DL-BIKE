# coding=utf-8
#
# :author pyx0622@gmail.com
# :date 2016.08.13
# :table data_source

from dao.base import BaseDao

class DataSourceDao(BaseDao):

    def __init__(self):
        super(DataSourceDao, self).__init__()
        self.table = "data_source"
        self.fields_map = {
            "id":          self.constant.TYPE_INT,
            "name":        self.constant.TYPE_STRING, # 来源名称, 对应 header中的键名
        }

