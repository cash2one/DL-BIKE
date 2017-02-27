# coding=utf-8

# @Time    : 2/14/17 21:26
# @Author  : panda (panyuxin@moseeker.com)
# @File    : headers.py
# @DES     : 

import random
from util.common import ObjectDict

## 随机 User_agent
COMMON_UA = [
    'Mozilla/5.0 (Linux; Android 6.0.1; Nexus 5 Build/MOB30Y) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/37.0.0.0 Mobile MQQBrowser/6.2 TBS/036555 Safari/537.36 MicroMessenger/6.3.22.821 NetType/WIFI Language/zh_CN',
    'Mozilla/5.0 (iPhone; CPU iPhone OS 10_2_1 like Mac OS X) AppleWebKit/602.4.6 (KHTML, like Gecko) Mobile/14D27 MicroMessenger/6.5.5 NetType/WIFI Language/zh_CN'
]

COMMON_HEADER = {
    "user-agent" : random.choice(COMMON_UA)
}

## 数据来源
DATA_SOURCE = ObjectDict({
    "beijing_app": ObjectDict({
        # 北京市公共自行车App
        "source_id": 1,
        "header": ObjectDict({
            'content-type': "application/x-www-form-urlencoded",
            'cookie': "JSESSIONID=1F1E59738AD63B96CAB53317DD732787",
            'user-agent': "mobileapp/1.0.4 (iPhone; iOS 10.2.1; Scale/2.00)clientVersion/iOS-1.0.4;clientType/bjbike_app",
        })
    }),
    "beijing_wechat": ObjectDict({
        # 微信城市服务，北京公共自行车查询
        "source_id": 2,
        "header_html": ObjectDict({
            # html 页面 header
            'Host': 'www.bjjtw.gov.cn',
            'Referer': 'http://www.bjjtw.gov.cn/wx/app/weixin/bicycle/main/al?character=publicCityServer',
            'Accept': '*/*',
            'X-Requested-With': 'XMLHttpRequest',
            'Accept-Encoding': 'gzip, deflate',
            'Accept-Language': 'zh-CN,en-US;q=0.8',
            'cookie': 'KKDvkqh6eK=MDAwM2IyNGNiNjAwMDAwMDAwMDcwFRkmAjUxNDcxMTAxNjU5',
            'User-Agent': 'Mozilla/5.0 (Linux; Android 6.0.1; Nexus 5p Build/MOB30Y) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/37.0.0.0 Mobile MQQBrowser/6.2 TBS/036555 Safari/537.36 MicroMessenger/6.3.22.821 NetType/WIFI Language/zh_CN',

        }),
        "header_json": ObjectDict({
            # json 列表 header
            'Host': 'bjggzxc.btic.org.cn',
            'Origin': 'http://bjggzxc.btic.org.cn',
            'Referer': 'http://www.bjjtw.gov.cn/wx/app/weixin/bicycle/main/al?character=publicCityServer',
            'Accept': 'application/json, text/javascript, */*; q=0.01',
            'X-Requested-With': 'XMLHttpRequest',
            'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
            'Accept-Encoding': 'gzip, deflate',
            'Accept-Language': 'zh-CN,en-US;q=0.8',
            'User-Agent': 'Mozilla/5.0 (Linux; Android 6.0.1; Nexus 6 Build/MOB30Y) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/37.0.0.0 Mobile MQQBrowser/6.2 TBS/036555 Safari/537.36 MicroMessenger/6.3.22.821 NetType/WIFI Language/zh_CN',
        })
    }),
    "dingda_app": ObjectDict({
        # 叮嗒出行App
        "source_id": 3,
        "header": ObjectDict({
            'user-agent': "DDTrip/1.4.2 (iPhone; iOS 10.2.1; Scale/2.00)",
            'source': "IOS",
            'version': "1.4.0",
        })
    }),
    "xian_app": ObjectDict({
        "source_id": 4,
        "header": ObjectDict({
            'content-type': "application/x-www-form-urlencoded",
            'cookie': "PHPSESSID=abtgvitarmb8cgs85a1jcm1c63",
            'user-agent': "2.0.0 (iPhone; iOS 10.2.1; zh_CN)",
            'host': "bike.phioc.cn",
            'accept-encoding': "gzip",
        })
    }),
    "nanjing_wechat": ObjectDict({
        "source_id": 5,
        "header": ObjectDict({
            'Host': 'www.njlrsoft.cn',
            'Referer': 'http://www.njlrsoft.cn/bicycle/lwzj.html?openid=oybL6s2gsJQ7UqDo7FSxIVQRk3fs&flag=wx',
            'Accept': 'application/json',
            'X-Requested-With': 'XMLHttpRequest',
            'Accept-Encoding': 'gzip, deflate',
            'Accept-Language': 'zh-CN',
            'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 10_2_1 like Mac OS X) AppleWebKit/602.4.6 (KHTML, like Gecko) Mobile/14D27 MicroMessenger/6.5.5 NetType/WIFI Language/zh_CN',
        })
    }),
})