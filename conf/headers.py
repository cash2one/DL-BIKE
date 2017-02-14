# coding=utf-8

# @Time    : 2/14/17 21:26
# @Author  : panda (panyuxin@moseeker.com)
# @File    : headers.py
# @DES     : 

# Copyright 2016 MoSeeker

## USER_AGENT
COMMON_UA = {
    'User-Agent': 'Mozilla/5.0 (Linux; Android 6.0.1; Nexus 5 Build/MOB30Y) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/37.0.0.0 Mobile MQQBrowser/6.2 TBS/036555 Safari/537.36 MicroMessenger/6.3.22.821 NetType/WIFI Language/zh_CN',
}

### BEIJING
BEIJING_HTML_HEADERS = {
    'Host': 'www.bjjtw.gov.cn',
    'Referer': 'http://www.bjjtw.gov.cn/wx/app/weixin/bicycle/main/al?character=publicCityServer',
    'Accept': '*/*',
    'X-Requested-With': 'XMLHttpRequest',
    'Accept-Encoding': 'gzip, deflate',
    'Accept-Language': 'zh-CN,en-US;q=0.8',
    'cokie': 'KKDvkqh6eK=MDAwM2IyNGNiNjAwMDAwMDAwMDcwFRkmAjUxNDcxMTAxNjU5',
    'User-Agent': 'Mozilla/5.0 (Linux; Android 6.0.1; Nexus 5 Build/MOB30Y) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/37.0.0.0 Mobile MQQBrowser/6.2 TBS/036555 Safari/537.36 MicroMessenger/6.3.22.821 NetType/WIFI Language/zh_CN',
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
    'User-Agent': 'Mozilla/5.0 (Linux; Android 6.0.1; Nexus 5 Build/MOB30Y) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/37.0.0.0 Mobile MQQBrowser/6.2 TBS/036555 Safari/537.36 MicroMessenger/6.3.22.821 NetType/WIFI Language/zh_CN',
}