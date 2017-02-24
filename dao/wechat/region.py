# coding=utf-8
#
# :author pyx0622@gmail.com
# :date 2016.08.13
# :table region


from dao.base import BaseDao

class RegionDao(BaseDao):

    def __init__(self):
        super(RegionDao, self).__init__()
        self.table = "region"
        self.fields_map = {
            "rid":          self.constant.TYPE_INT, # 地区编号
            "cid":          self.constant.TYPE_INT, # 所属城市编号
            "pname":        self.constant.TYPE_STRING, # 省（州）名称
            "cname":        self.constant.TYPE_STRING, # 城市名称
            "rname":        self.constant.TYPE_STRING,  # 地区名称
        }

