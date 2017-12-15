# coding=utf-8


"""
说明:
constant配置常量规范：
1.常量涉及通用业务逻辑定义，即同时适用于聚合号和企业号
2.系统常量定义在顶部，业务常量定义在底部。
3.使用分割线区分系统、业务常量
4.常量配置添加注释

常量使用大写字母
例如 SUCCESS = "成功"
"""

# status_message
RESPONSE_SUCCESS = "SUCCESS"
RESPONSE_FAILURE = "FAILURE"

API_SUCCESS = 0
API_FAILURE = 1

NOT_AUTHORIZED = "用户未被授权请求"
NO_DATA = "Ta在地球上消失了"
UNKNOWN_DEFAULT = "正在努力处理您的问题"

# 微信客户端类型
CLIENT_WECHAT = 1
CLIENT_NON_WECHAT = 2
CLIENT_TYPE_IOS = 100
CLIENT_TYPE_ANDROID = 101
CLIENT_TYPE_WIN = 102
CLIENT_TYPE_UNKNOWN = 103

# 入库字段类型
TYPE_INT = 1
TYPE_JSON = 2
TYPE_FLOAT = 3
TYPE_TIMESTAMP = 4
TYPE_STRING = 5  # 会过滤xss
TYPE_STRING_ORIGIN = 6  # 不过滤xss

# 日期、时间规范
TIME_FORMAT = "%Y-%m-%d %H:%M:%S"
TIME_FORMAT_PURE = "%Y%m%d%H%M%S"
TIME_FORMAT_DATEONLY = "%Y-%m-%d"
TIME_MINUTE_ONLY = "%H:%M"
TIME_FORMAT_MINUTE = "%Y-%m-%d %H:%M"
TIME_FORMAT_MSEC = "%Y-%m-%d %H:%M:%S.%f"
JD_TIME_FORMAT_DEFAULT = "-"
JD_TIME_FORMAT_FULL = "{}-{:0>2}-{:0>2}"
JD_TIME_FORMAT_JUST_NOW = "刚刚"
JD_TIME_FORMAT_TODAY = "今天 {:0>2}:{:0>2}"
JD_TIME_FORMAT_YESTERDAY = "昨天 {:0>2}:{:0>2}"

# 数据库规范化常量
STATUS_INUSE = 1
STATUS_UNUSE = 0

BAIDU_POI_Q = ["美食", "旅馆", "小区"]

# HZtrip
# stop
STOP_STATE = {
    "0":"暂无",
    "1":"泊位已满",
    "2":"泊位紧张",
    "3":"少量泊位",
    "4":"泊位宽裕",
}

# bus line alert
BUS_LINE_ALERT_MORNING_PEAK_START = "07:00"
BUS_LINE_ALERT_MORNING_PEAK_END = "09:00"
BUS_LINE_ALERT_EVENING_PEAK_START = "16:30"
BUS_LINE_ALERT_EVENING_PEAK_END = "18:30"

# pubsub ads
CHANNEL_ADS = "channel_ads"
CHANNEL_ADS_SIGNLE = "channel_ads_single"
ADS_CONTENT = "【红包】摇号没中签？送你红包，最高888元！#吱口令#长按复制此消息，打开支付宝就能领取！yLl4je03Ux"
