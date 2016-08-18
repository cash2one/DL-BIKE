# coding=utf-8

'''
说明:
constant配置常量规范：
1.常量涉及通用业务逻辑定义，即同时适用于聚合号和企业号
2.系统常量定义在顶部，业务常量定义在底部。
3.使用分割线区分系统、业务常量
4.常量配置添加注释

常量使用大写字母，字符串需要时标注为unicode编码
例如 SUCCESS = u"成功"

'''

# ++++++++++系统常量++++++++++

## 返回错误

### status_code默认错误返回
RESPONSE_SUCCESS = u"success"
RESPONSE_FAILED = u"failed"

## 入库字段类型
TYPE_INT = 1
TYPE_JSON = 2
TYPE_FLOAT = 3
TYPE_TIMESTAMP = 4
TYPE_STRING = 5  # 会过滤xss
TYPE_STRING_ORIGIN = 6  # 不过滤xss

## 日期、时间规范
TIME_FORMAT = u"%Y-%m-%d %H:%M:%S"
TIME_FORMAT_PURE = u"%Y%m%d%H%M%S"
TIME_FORMAT_DATEONLY = u"%Y-%m-%d"
TIME_FORMAT_MINUTE = u"%Y-%m-%d %H:%M"
TIME_FORMAT_MSEC = u"%Y-%m-%d %H:%M:%S.%f"
JD_TIME_FORMAT_DEFAULT = u"-"
JD_TIME_FORMAT_FULL = u"{0}-{:0>2}-{:0>2}"
JD_TIME_FORMAT_JUST_NOW = u"刚刚"
JD_TIME_FORMAT_TODAY = u"今天 {:0>2}:{:0>2}"
JD_TIME_FORMAT_YESTERDAY = u"昨天 {:0>2}:{:0>2}"
JD_TIME_FORMAT_THIS_YEAR = u"{:0>2}-{:0>2}"

STATUS_ONUSE = 1
STATUS_UNUSE = 0


# ++++++++++业务常量+++++++++++

COMMON_UA = {
    'User-Agent': 'Mozilla/5.0 (Linux; Android 6.0.1; Nexus 5 Build/MOB30Y) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/37.0.0.0 Mobile MQQBrowser/6.2 TBS/036555 Safari/537.36 MicroMessenger/6.3.22.821 NetType/WIFI Language/zh_CN',
}

## USER_AGENT
BEIJING_HTML_HEADERS = {
    'Host': 'www.bjjtw.gov.cn',
    'Referer': 'http://www.bjjtw.gov.cn/wx/app/weixin/bicycle/main/al?character=publicCityServer',
    'Accept': '*/*',
    'X-Requested-With': 'XMLHttpRequest',
    'Accept-Encoding': 'gzip, deflate',
    'Accept-Language': 'zh-CN,en-US;q=0.8',
    'cokie': 'KKDvkqh6eK=MDAwM2IyNGNiNjAwMDAwMDAwMDcwFRkmAjUxNDcxMTAxNjU5'
}

BEIJING_JSON_HEADERS = {
    'Host': 'bjggzxc.btic.org.cn',
    'Origin': 'http://bjggzxc.btic.org.cn',
    'Referer': 'http://www.bjjtw.gov.cn/wx/app/weixin/bicycle/main/al?character=publicCityServer',
    'Accept': 'application/json, text/javascript, */*; q=0.01',
    'X-Requested-With': 'XMLHttpRequest',
    'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
    'Accept-Encoding': 'gzip, deflate',
    'Accept-Language': 'zh-CN,en-US;q=0.8',
}




