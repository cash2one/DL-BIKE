# -*- coding: utf-8 -*-

'''
说明:
constant配置常量规范：
1.常量涉及业务逻辑定义
2.系统常量定义在顶部，业务常量定义在底部。
3.使用分割线区分系统、业务常量
4.常量配置添加注释
'''

# ++++++++++系统常量++++++++++
## 时间规范
TIME_FORMAT = u"%Y-%m-%d %H:%M:%S"
TIME_FORMAT_PURE = u"%Y%m%d%H%M%S"
TIME_FORMAT_DATEONLY = u"%Y-%m-%d"
TIME_FORMAT_MINUTE = u"%Y-%m-%d %H:%M"
TIME_FORMAT_MSEC = u"%Y-%m-%d %H:%M:%S.%f"

## 返回错误

### status_code默认错误返回
RESPONSE_SUCCESS = u"成功"
RESPONSE_FAILED = u"操作失败"
RESPONSE_COMMON = u"未知错误"

### Exception
EXCEPTION_SESSION_INDEX_ERROR = u"session index error"


# ++++++++++业务常量+++++++++++
