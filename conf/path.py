# coding=utf-8

# @Time    : 2/9/17 22:40
# @Author  : panda (panyuxin@moseeker.com)
# @File    : path.py
# @DES     :

# 外部服务地址
BAIDU_WEBAPI_PLACE_POI_LIST = "http://api.map.baidu.com/place/v2/search"
BAIDU_WEBAPI_GEOCONV_LNGLAT = "http://api.map.baidu.com/geoconv/v1/"
BAIDU_WEBAPI_DIRECTION = "http://api.map.baidu.com/direction/v1"

QQ_WEBAPI_PLACE_POI_LIST = "http://apis.map.qq.com/ws/geocoder/v1/"
QQ_WEBAPI_GEOCONV_LNGLAT = "http://apis.map.qq.com/ws/coord/v1/translate"

# hzrip
HZTRIP_STOP = "http://api.busditu.com/hangzhou/parking/nearby/"
HZTRIP_YAOHAO = "https://sp0.baidu.com/9_Q4sjW91Qh3otqbppnN2DJv/pae/common/api/yaohao"
HZTRIP_BIKE = "http://c.ggzxc.com.cn/wz/np_getBikesByWeiXin.do"
HZTRIP_BIKE_NO = "http://c.ggzxc.com.cn/wz/np_getNPByNum.do"
HZTRIP_BUS = "https://publictransit.dtdream.com/v1/bus/{}"


# weapp
DINGDA_NEARBY_LIST = "http://bike-a.api.dingdatech.com/service/bicycle/stations"
BEIJING_NEARBY_LIST = "http://api.nengren-tech.com/bj_bicycleLease/query/queryStation.do"
XIAN_NEARBY_LIST = "http://bike.phioc.cn/api/get_around"
NANJING_LIST = "http://www.njlrsoft.cn/bicycle/assets/js/site.json"

# wechat
WECHAT_ACCESS_TOKEN = "https://api.weixin.qq.com/cgi-bin/token?grant_type=client_credential&appid={0}&secret=={1}"
WECHAT_USER_INFO = "https://api.weixin.qq.com/cgi-bin/user/info?access_token={0}&openid={1}&lang=zh_CN"
WECHAT_TEMPALTE = "https://api.weixin.qq.com/cgi-bin/message/template/send?access_token={0}"