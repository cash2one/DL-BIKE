# coding=utf-8

# @Time    : 2/21/17 14:33
# @Author  : panda (panyuxin@moseeker.com)
# @File    : daily_sign_in.py
# @DES     : 

import http.client

from util.tool.date_tool import curr_now

def qyer_sign_in():

    """穷游客户端签到"""
    conn = http.client.HTTPConnection("open.qyer.com")

    payload = "account_s=fef74474cd9678792d86e83dfafbfb9e&client_id=qyer_ios&client_secret=cd254439208ab658ddf9&count=20&lat=31.19774147548028&lon=121.4274459760588&oauth_token=0b03e0779e7c7daf114945ef1df24ec6&page=1&track_app_channel=AppStore&track_app_version=7.4&track_device_info=iPhone&track_deviceid=39DA2458-316C-70AE-F956-B3C46ED9CCE6&track_os=ios10.2.1&track_user_id=1793208&v=1"

    headers = {
        'content-type': "application/x-www-form-urlencoded",
        'host': "open.qyer.com",
        'accept': "*/*",
        'connection': "keep-alive",
        'cookie': 'als=0; _guid=c50082bd-15a4-c693-dc03-24ffffdcfad0; init_refer=; new_session=1; new_uv=32; session_time=1509463301.126; __utma=253397513.1667471721.1476627137.1507943677.1509463300.32; __utmb=253397513.1.10.1509463300; __utmc=253397513; __utmt=1; __utmz=253397513.1476627137.1.1.utmcsr=(direct)|utmccn=(direct)|utmcmd=(none); cdb_auth=f865Zzg1iKKqjyGeI%2BFCAAjOHMUi5kKpmzy%2BCaSC7kBfXWQ8NTfbshapHz7Q09%2BBI8G88gltuMU9igrvFlCDRNrpcl6P7A; cdb_cookietime=2952000; _fmdata=F602CAD3DC0947ADDC728EFB1EE7D8CDB56E1F3A38DE5E22D1E03FA75AB7EB02EBF6A966EEA46ADD01E8A2D76E141A7546FF8737A1689E3D; fingerprint=49Gr28qN1TX5HNm3pSBhKvL1z2epS3TfkVgIaAGU6FIlZl3t1486992556072; wdata_token=49Gr28qN1TX5HNm3pSBhKvL1z2eptaQgegUzJdCwC1waqD2I1486992556074',
        'user-agent': "QYER/7.12.4 (iPhone; iOS 11.0.3; Scale/2.00)",
    }

    conn.request("POST", "/qyer/mileage/sign/add_mileage", payload, headers)

    res = conn.getresponse()
    data = res.read()

    print("[qyer][time:{}][res:{}]".format(curr_now(), data.decode("utf-8")))

def smzdm_sign_in():

    """什么值得买客户端签到"""
    conn = http.client.HTTPSConnection("api.smzdm.com")

    payload = "f=iphone&sign=7DC26095717492A87146E9D4D71AA598&sk=uiWkBkg57AP5tggciZymf6DkP9ohEFVwAdlOglDChPPdRpXLw2xaIUFxAfCs8bzi&time=1507907588&token=MmQ0ZDB8MTUwODk5MzQ2OXw2NDE4MjE0MDEyfDQzMTJkMWNjMDU0NGJjNzcxOGYxNDJlMzgwODE1MTRh&v=8.3&weixin=1"

    headers = {
        'host': "api.smzdm.com",
        'content-type': "application/x-www-form-urlencoded",
        'cookie': "ab_test=b; device_id=uDk0xR1zF3nHICXl8eYhCaLUYGRXo4TppwRA8BMFort5um+s9s/lIw==; device_name=iPhone 6s; device_push=notifications_are_disabled; device_s=uDk0xR1zF3nHICXl8eYhCaLUYGRXo4TppwRA8BMForudSM4DDGPB3wFJMeDGKwRzZuH3pEdyh8=; device_smzdm=iphone; device_smzdm_version=8.3; device_system_version=11.0.3; device_type=iPhone8,1; login=1; network=WiFi_Net; partner_id=0; partner_name=AppStore; phone_sort=6; sess=MmQ0ZDB8MTUwODk5MzQ2OXw2NDE4MjE0MDEyfDQzMTJkMWNjMDU0NGJjNzcxOGYxNDJlMzgwODE1MTRh; smzdm_id=6418214012; ga=GA1.2.1324618150.1503809524; Hm_lvt9b7ac3d38f30fe89ff0b8a0546904e58=1507648237; device_id=6055455861507648237322450ae0292c4aeeb071ca659e6e0ea6cfd11; sess=MmQ0ZDB8MTUxMTUzNjIzMnw2NDE4MjE0MDEyfGQ5ZmZlNWQ2OTE1NWZmNjRhMmNlMjdiZTljYTk3OTEz; user=sina_tgrlc%7C6418214012; smzdm_user_source=98EFC26EF7B3DE478B9FEDB199BC5FB2; ckguid=57u5eKxRhNAlwkb2V1PE4nw7; jsluid=2bfd8c8f629d4da9206e1a788bd9fc4e",
        'user-agent': "SMZDM/8.3 (iPhone; iOS 11.0.3; Scale/2.00)",
        'accept-language': "zh-Hans-CN;q=1, en-CN;q=0.9, zh-Hant-CN;q=0.8",
    }

    conn.request("POST", "/v1/user/checkin", payload, headers)

    res = conn.getresponse()
    data = res.read()

    print("[smzdm][time:{}][res:{}]".format(curr_now(), data.decode("utf-8")))


def music_163_sign_in():

    """网易云音乐签到"""
    conn = http.client.HTTPConnection("music.163.com")

    payload = "params=04F1A0AB8150EFD085BC839891D19E2E488A2D6C2924C5589260A62E82B1A0D3BA7AC29333EDAA68300EE4FE29CFD7407CD065FD9D8BA0153B98A3AFE422456DF5B4AF6FEFB7011FC85EA28E8CEDADA4233BB43F0F8B76F24D9AB171B538220CD0398941677B9A89C628F424FB2AA0984E7F0F7D305BC5E35F5CF756D6BBB996B3F64B78E30003F2BD1D9529165DB9B95EE290D58921FD5D7D507433E66DF78F7CDDFC5F2C86D11134D14C4B9B162C8977B4A63B5BB595B0FAB0D94F59DCAF14C9C699D5D439369EAD11BA4BECCD7A3B0403D0DA14A27CC6B3C203788789AF492F3143287CEC1B7337F1EDBB99350C42DAC41BEAA61A53C40E8843ECB98BF6067CD065FD9D8BA0153B98A3AFE422456DF5B4AF6FEFB7011FC85EA28E8CEDADA4BB0B520B36F7B62359FB9EB25282CC53A4C855FE4D769B5AB9C1D5DB9B54C3B2908C2C2A2120DEAD8E028BD6AB85403EA94369B1DA20D473D69042283FAC324869C1115961DA65615815ABFD139405586D5B7732442D99A133AB15391677B6A00898EBF741BDFBE28C530FF426061A398D3DEB528DEA5D61EABCD3CD5F422ECEF2908E4EE1670EFB61C5211C87369F6E636D2FFFAE5D4D6358E104D39B42D6E9D4356D88F4AA9D810259CC200D69CAB6F681FC595E0FB0A228CBDB657F0F5B2B14A4DD97D79CE7E7DC3A3BC17B29C0C6107390459EEF14A4D43B10BB9099BFE8A2C299DEA6763894248443BB2C40B0A9952E6ACF1C2F1F50ED3695822C3532B288240948A06BD80FF90823B9C06AA93E4C888336B2B3BAAF301A662B2BD332B3C1B5F865E0C0F565830D262C482C2C74A1D185CB6DCAF83656F1F43B87D0E72865115AD72EA6A613F467B50ED19A51EA5FA1ED92A570EFEAA6B49207CB2B6D1F"

    headers = {
        'host': "music.163.com",
        'content-type': "application/x-www-form-urlencoded",
        'cookie': "os=iPhone OS; osver=10.2.1; appver=3.7.5; deviceId=d03ab28a26a9b5b35d3dee25c3eb00d2; MUSIC_U=61a5d719c83ecbfc5c7b8435f560458e1592dcc50ab2a078cf3c61ff4a7ec5e0ad2ea5269380b8893eb7658aeefa351d365b7c0d8e97a004c3061cd18d77b7a0",
        'accept-encoding': "gzip",
    }

    conn.request("POST", "/eapi/point/dailyTask", payload, headers)

    conn.getresponse()

    print("[163music][time:{}]".format(curr_now()))

def nuomi_sign_in():

    """百度糯米签到"""
    conn = http.client.HTTPConnection("180.97.93.28")

    headers = {
        'host': "app.nuomi.com",
        'cookie': "STOKEN=a6a802f9721b1ccb9df862df46eecc1f8b10b7978af359d9f51bf31935a9cf39; bn_na_ctag=W3siayI6Imljb25fNCIsInMiOiJ0dWFuIiwieCI6IiIsInYiOiIxMDkwMDAwMCIsInQiOiIxNDg4OTg0MTczIn1d; bn_na_home_entry=W3siayI6IjQiLCJzIjoidG9waWNvbiIsIngiOiIiLCJ2IjoiMTA5MDAwMDAiLCJ0IjoiMTQ4ODk4NDE3MyJ9XQ==; bn_na_copid=7f889be41fa4bcfb75df92aa29a13e93; BAINUOCUID=812b949966edc7a0043332b9f0e7819898906605; bn_na_component_sinfo=%7B%22pl_sinfo%22%3A%22%7B%5C%22NA%5C%22%3A%5B777%2C523%2C326%2C533%2C253%2C218%2C539%2C327%2C375%2C585%2C413%2C648%2C347%2C734%2C615%2C382%2C378%2C671%2C760%2C452%2C607%2C782%2C619%2C455%2C552%2C636%2C605%2C683%2C628%2C633%2C642%2C771%2C654%2C655%2C665%2C673%2C675%2C678%2C695%2C696%2C700%2C737%2C711%2C792%2C728%2C804%2C748%2C773%2C762%2C774%2C781%2C803%5D%7D%5Cn%22%2C%22app_v%22%3A%227.1.0%22%7D; bn_na_smallflow_info=%7B%22pl_sinfo%22%3A%22%7B%5C%22NA%5C%22%3A%5B777%2C523%2C326%2C533%2C253%2C218%2C539%2C327%2C375%2C585%2C413%2C648%2C347%2C734%2C615%2C382%2C378%2C671%2C760%2C452%2C607%2C782%2C619%2C455%2C552%2C636%2C605%2C683%2C628%2C633%2C642%2C771%2C654%2C655%2C665%2C673%2C675%2C678%2C695%2C696%2C700%2C737%2C711%2C792%2C728%2C804%2C748%2C773%2C762%2C774%2C781%2C803%5D%7D%5Cn%22%7D; UID=161275167; BAIDUID=ED6800311E782FD7EC2BDACABD76C793:FG=1; bn_v=7.1.0; na_pdqab_new=812b949966edc7a0043332b9f0e7819898906605; BDUSS=FkRzJMMm9KbmxGMHE2SkY1U01IekdTMmt-UWZ4VHl2cEhGQUhZaUdodzFwcUZZSVFBQUFBJCQAAAAAAAAAAAEAAAAf3ZwJt7nQobezAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAADUZelg1GXpYcG; na_qab=c75f7a1f7f8196b59ffeb9f0c5553ab4; moudle_pdqab=voucher; access_log=27a05c44016d5fac9e924fb351caaf89",
        'user-agent': "Bainuo/7.1.0 (iPhone; iOS 10.2.1; Scale/2.00)",
    }

    conn.request("GET",
                 "/naserver/user/memberpointreceive?appid=ios&appkey=sFTRwpfNpZihllpqhpionpCmnJ%2Box6WSztKXZJ6ppqGeVI2DpM6Yq5qgqp2Gb1ua0adZXVjSqdTJ2ZeqUm5ZoqqhzspW3w%3D%3D&bduss=FkRzJMMm9KbmxGMHE2SkY1U01IekdTMmt-UWZ4VHl2cEhGQUhZaUdodzFwcUZZSVFBQUFBJCQAAAAAAAAAAAEAAAAf3ZwJt7nQobezAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAADUZelg1GXpYcG&bnjsv=1.4&channel=com_dot_apple&cityid=200010000&compId=points&compV=1.7.0&cuid=812b949966edc7a0043332b9f0e7819898906605&device=iPhone&ha=5&lbsidfa=00000000-0000-0000-0000-000000000000&location=31.328280%2C121.388300&net=wifi&os=10.2&outer_channel=&page_type=component&power=0.64&sheight=1334&sign=5ab0c43622562c72db15e578654b7714&swidth=750&terminal_type=ios&timestamp=1488984174393&tn=ios&uuid=812b949966edc7a0043332b9f0e7819898906605&v=1.1.0",
                 headers=headers)

    res = conn.getresponse()
    data = res.read()

    print("[nuomi][time:{}][res:{}]".format(curr_now(), data.decode("utf-8")))

def gewara_sign_in():

    """格瓦拉签到"""
    conn = http.client.HTTPSConnection("m.gewara.com")

    payload = ""

    headers = {
        'host': "m.gewara.com",
        'accept': "text/javascript, text/html, application/xml, text/xml, */*",
        'x-requested-with': "XMLHttpRequest",
        'if-modified-since': "0",
        'cache-control': "no-cache",
        'content-type': "application/x-www-form-urlencoded",
        'origin': "https://m.gewara.com",
        'user-agent': "Mozilla/5.0 (iPhone; CPU iPhone OS 10_2_1 like Mac OS X) AppleWebKit/602.4.6 (KHTML, like Gecko) Mobile/14D27 GewaraMovie/8.1.0 appkey/iphoneV64 appSource/AS02 apptype/cinema osType/IPHONE from/appiphoneV64 deviceId/00000000-0000-0000-0000-000000000000 uuid/374E6744-BA1D-4619-8C87-81E077924D1D citycode/310000",
        'referer': "https://m.gewara.com/touch/app/point/index.xhtml",
    }

    conn.request("POST", "/touch/app/point/getDayPoint.xhtml", payload, headers)

    res = conn.getresponse()
    data = res.read()

    print("[gewara][time:{}][res:{}]".format(curr_now(), data.decode("utf-8")))

def ctrip_sign_in():

    """携程签到"""

    conn = http.client.HTTPSConnection("m.ctrip.com")

    payload = "{\"head\":{\"cid\":\"12021067210004192157\",\"ctok\":\"\",\"cver\":\"701.002\",\"lang\":\"01\",\"sid\":\"8890\",\"syscode\":\"12\",\"auth\":\"83B18B3D138789BD220EC796908422BAFAE5CCC3779EC87911823971FFE6EDBE\",\"extension\":[{\"name\":\"protocal\",\"value\":\"file\"}]},\"contentType\":\"json\"}"

    headers = {
        'host': "m.ctrip.com",
        'content-type': "application/json",
        'origin': "file://",
        'cookie': "_jzqco=%7C%7C%7C%7C1507944112259%7C1.905210666.1455900703011.1507697742717.1507944111182.1507697742717.1507944111182.0.0.0.44.44; MKT_Pagesource=H5; _bfa=1.1444525448857.2mqlyq.1.1444525448857.1507944111034.6.8.10320668463; cticket=83B18B3D138789BD220EC796908422BA759D34559608972085D5FE39FBF9C670; isNonUser=false; _n_cid=12021067210004192157; _RF1=180.153.219.16; _RGUID=7a4492c4-fc70-4794-9745-2411e3573f4c; _RSG=KU4SyJia4f7CzpLZ7195T9; page_time=1502104817001%2C1505881602136%2C1507697734006%2C1507697742882; fingerprint=DBTAlxNWxRDvawFA3Fom1492435801299; wdata_token=SXv3jUHG4yxA95tiH411bYckGc90mCNRup8yjuGxfGT5dFW1492435801301; _ga=GA1.2.499933121.1444525450",
        'accept': "application/json",
        'user-agent': "Mozilla/5.0 (iPhone; CPU iPhone OS 11_0_3 like Mac OS X) AppleWebKit/537.51.1 (KHTML, like Gecko) Mobile/11B508_eb64__Ctrip_CtripWireless_7.7.1_CtripAPP_iOS_soa",
    }

    conn.request("POST", "/restapi/soa2/11631/json/CheckIn", payload, headers)

    res = conn.getresponse()
    data = res.read()

    print("[ctrip][time:{}][res:{}]".format(curr_now(), data.decode("utf-8")))


def jd_sign_in():

    """ 京东签到"""

    conn = http.client.HTTPSConnection("ld.m.jd.com")

    headers = {
        'host': "ld.m.jd.com",
        'cookie': "__mjdv=direct|-|none|-; __utmmobile=0xa445f15745f76661.1486907576000.1486907576000.1486907576000.3; abtest=20170206210701441_00; __jda=71854095.908336774.1486385897.1488988831.1489216298.6; __jdb=71854095.1.908336774|6.1489216298; __jdc=71854095; __jdu=908336774; __jdv=71854095|direct|-|none|-|1489216298331; mba_muid=908336774.86.1489216298385; mba_sid=86.5; pre_seq=3; pre_session=e2d83aac95815af9c3888b81fd602c66165d700b|99; pt_key=app_openAAFYw6MoADC4-jVP-jKqSQD2yQln2iDdi4MwiH-PDxTikyfujLVO3HoCDgfC3vJYzCCP1eULrgE; pt_pin=pan7an; pwdt_id=pan7an; sid=8d56e4fb70fa5edc6fca100767d97d8w; mobilev=touch; _jrda=1",
        'accept': "application/json, text/javascript, */*; q=0.01",
        'user-agent': "jdapp;iPhone;5.8.0;10.2.1;e2d83aac95815af9c3888b81fd602c66165d700b;network/wifi;supportApplePay/1;pv/86.4;pap/JA2015_311210|5.8.0|IOS 10.2.1;psn/e2d83aac95815af9c3888b81fd602c66165d700b|99;psq/3;ads/;ref/JDMainPageViewController;jdv/0|;usc/direct;adk/;umd/none;ucp/-;utr/-;Mozilla/5.0 (iPhone; CPU iPhone OS 10_2_1 like Mac OS X) AppleWebKit/602.4.6 (KHTML, like Gecko) Mobile/14D27",
        'referer': "https://ld.m.jd.com/userBeanHomePage/getLoginUserBean.action?lng=121.376936&lat=31.324753&un_area=2_2824_51912_0&sid=8d56e4fb70fa5edc6fca100767d97d8w",
        'x-requested-with': "XMLHttpRequest",
    }

    conn.request("GET", "/SignAndGetBeans/signStart.action?sid=8d56e4fb70fa5edc6fca100767d97d8w", headers=headers)

    res = conn.getresponse()
    data = res.read()
    print("[jd][time:{}][res:{}]".format(curr_now(), data.decode("utf-8")))

def baidumap_sign_in():

    """ 百度地图签到"""

    conn = http.client.HTTPConnection("client.map.baidu.com")

    payload = ""

    headers = {
        'host': "client.map.baidu.com",
        'content-type': "application/x-www-form-urlencoded",
        'cookie': "BDUSS=Edxc1MtQWszRHJzbU9CNG9Da1E5cDhxWn5nT2tYYUZPUmhlc0NDbWZ0VWhWYUpaTUFBQUFBJCQAAAAAAAAAAAEAAAAf3ZwJt7nQobezAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACHIelkhyHpZd; BAIDUID=1D43E5A7AB576D4D145FE1F0C0F0E710:FG=1; BIDUPSID=236E51D87EDDDBED261296F61F127CE5; PSTM=1450593054",
        'user-agent': "IphoneCom/9.7.3 (iPhone; iOS 10.2.1; Scale/2.00)",
        'accept-language': "zh-Hans-CN;q=1, en-CN;q=0.9, zh-Hant-CN;q=0.8",
    }

    conn.request("POST",
                 "/usersystem/user/signin/?ctm=1489218201.477000&glr=Adreno&dpi=(326%2C326)&cpu=ARMv7&sv=9.7.3&phonebrand=&channel=1008648b&patchver=&city=289&isart=&sinan=cqYJcogEWV4-b5Bcdecf0uw92&os=iphone10.200000&loc_y=3653069.782598&cuid=30d2343a40812e37b98fa8c653bdf20a&net=1&oem=&ver=1&loc_x=13513007.874462&mb=iPhone8%2C1&resid=01&co=460%3A11&poi_name=%E4%B8%8D%E9%80%89%E6%8B%A9%E5%9C%B0%E7%82%B9&screen=(750%2C1334)&glv=&sign=407807a5220ae63c55e7798428658c60",
                 payload, headers)

    res = conn.getresponse()
    data = res.read()
    print("[baidumap][time:{}][res:{}]".format(curr_now(), data.decode("utf-8")))

def umetrip_sign_in():

    """航旅纵横签到"""

    conn = http.client.HTTPConnection("ume1.umetrip.com")

    headers = {
        'host': "ume1.umetrip.com",
        'cookie': "JSESSIONID=30AD036CB3AB84053405243DE0B901BA; BIGipServerpool_hlzh_122.119.120.20_443=1870165882.20480.0000",
        'accept': "application/json, text/javascript, */*; q=0.01",
        'user-agent': "Mozilla/5.0 (iPhone; CPU iPhone OS 10_2_1 like Mac OS X) AppleWebKit/602.4.6 (KHTML, like Gecko) Mobile/14D27 Referer: http://ume1.umetrip.com/UmeAd/everyday/index.do?1=1&token=7up5ZpVPBpxmt+rjlpDbbsEa&sid=10159341$$3ccd35d067ee452297d6f2813802c66f",
        'x-requested-with': "XMLHttpRequest",
    }

    conn.request("GET", "/UmeAd/everyday/luck.do?sid=10159341%24%243ccd35d067ee452297d6f2813802c66f", headers=headers)

    res = conn.getresponse()
    data = res.read()
    print("[umetrip][time:{}][res:{}]".format(curr_now(), data.decode("utf-8")))

def xiami_sign_in():
    """虾米签到"""

    conn = http.client.HTTPConnection("spark.api.xiami.com")

    headers = {
        'host': "spark.api.xiami.com",
        'accept-language': "en;q=1, fr;q=0.9, de;q=0.8, zh-Hans;q=0.7, zh-Hant;q=0.6, ja;q=0.5",
        'user-agent': "walkman/5.8.8 (iPhone; iOS 10.2.1; Scale/2.00)",
        'connection': "close",
    }

    conn.request("GET",
                 "/api?access_token=1fd961bc3238ba56e5af0e1ec8f8e9cd&api_key=655bdb5fc1e0d21a53fce2cb8e1ba0ae&api_sig=5b68d95e8bb3dd49b8799ff4b724f8b2&app_v=5080800&call_id=1489219452.493017&ch=201200&device_id=00000000-0000-0000-0000-000000000000&h_uid=961864&lg=zh&method=task.sign-in&network=1&os_v=10.2.1&platform_id=2&proxy=0&resolution=750*1334&utdid=Vg6e8Fr8JcgDAPbzdTrtYzOg&v=5.0",
                 headers=headers)

    res = conn.getresponse()
    data = res.read()
    print("[xiami][time:{}][res:{}]".format(curr_now(), data.decode("utf-8")))

def futunn_sign_in():
    """富途牛牛签到"""
    conn = http.client.HTTPSConnection("www.futunn.com")

    headers = {
        'accept': "application/json, text/javascript, */*; q=0.01",
        'cookie': "_csrf=33G4bJIuSNeTM4e_4m7CkYRR65kdNyMp; UM_distinctid=15eff539f49dc-0c553eb610b8e5-63151074-1fa400-15eff539f4a989; tgw_l7_route=7587343559275141d1207d24944b360a; PHPSESSID=peht8qfnglfihn3b06m4ge76r3; web_sig=e5gMo5GN67FeOP96rOSniWe%2FoRDE0Symz8LXoAUb14jig3i9vfLm%2BQHjpumdaYiAUrONciE051723gKKFq8lBcf9q5tlz7TYEz6NOXls2ACMRQlEhm4Nu2Hs0DYVEmkE; uid=7172359; ci_sig=U8JbOVn43QlNJTSpL6yfHydNbGxhPTEwMDAwNTM4JmI9MjAxMTM2Jms9QUtJRENXblN2cWJ4UDkza3lYdW55ZTNNYXVJUWp2angydFlEJmU9MTUxMDExNDIyMiZ0PTE1MDc1MjIyMjImcj0yNDUyNDcwMjImdT0mZj0%3D; FUTU_TOOL_STAT_UNIQUE_ID=15075222235699620; CNZZDATA1256186977=204886084-1507517439-https%253A%252F%252Fpassport.futu5.com%252F%7C1507693377",
        'host': "www.futunn.com",
        'referer': "https://www.futunn.com/account/home",
        'user-agent': "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.86 Safari/537.36",
        'x-requested-with': "XMLHttpRequest",
        'dnt': "1",
        'cache-control': "no-cache"
    }

    conn.request("GET", "/site/sign-in", headers=headers)

    res = conn.getresponse()
    data = res.read()

    print("[futunn][time:{}][res:{}]".format(curr_now(), data.decode("utf-8")))


def mafengwo_fengmi_sign_in():
    """马蜂窝蜂蜜 ios 客户端签到"""
    conn = http.client.HTTPSConnection("m.mafengwo.cn")

    headers = {
        'accept': "application/json, text/javascript, */*; q=0.01",
        'x-requested-with': "XMLHttpRequest",
        'user-agent': "Mozilla/5.0 (Linux; Android 6.0.1; Nexus 5 Build/M4B30Z; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/61.0.3163.98 Mobile Safari/537.36 mfwappcode/com.mfw.roadbook mfwappver/8.0.4 mfwversioncode/445 mfwsdk/20140507 channel/TengXun mfwjssdk/1.1 mfwappjsapi/1.2",
        'referer': "https://m.mafengwo.cn/sales/activity/honey_center/",
        'accept-encoding': "gzip, deflate",
        'accept-language': "zh-CN,en-US;q=0.8",
        'cookie': '__idfa=00000000-0000-0000-0000-000000000000; __idfv=F6005B42-8F41-4C6F-80A4-6AD190FD3A7F; __openudid=F6005B42-8F41-4C6F-80A4-6AD190FD3A7F; PHPSESSID=82cf136e74qjc3rg79qlg5qh35; mfw_uid=9154997; __mfwlt=1509330923; __mfwlv=1509330923; __mfwvn=20; oad_n=a%3A3%3A%7Bs%3A3%3A%22oid%22%3Bi%3A2581%3Bs%3A2%3A%22dm%22%3Bs%3A16%3A%22mapi.mafengwo.cn%22%3Bs%3A2%3A%22ft%22%3Bs%3A19%3A%222017-10-25+22%3A21%3A00%22%3B%7D; UM_distinctid=15ec2f6c660146-00efefec2d986d-251f7468-3d10d-15ec2f6c662128; __mfwurd=a%3A3%3A%7Bs%3A6%3A%22f_time%22%3Bi%3A1506509504%3Bs%3A9%3A%22f_rdomain%22%3Bs%3A13%3A%22m.mafengwo.cn%22%3Bs%3A6%3A%22f_host%22%3Bs%3A1%3A%22m%22%3B%7D; __mfwuuid=59c7a7b7-5904-55f5-cbea-9460f64e4e15; uva=s%3A108%3A%22a%3A3%3A%7Bs%3A2%3A%22lt%22%3Bi%3A1506509504%3Bs%3A10%3A%22last_refer%22%3Bs%3A40%3A%22https%3A%2F%2Fm.mafengwo.cn%2Fsales%2F2217861.html%22%3Bs%3A5%3A%22rhost%22%3BN%3B%7D%22%3B; mfw_uuid=59c7a7b7-5904-55f5-cbea-9460f64e4e15',
        'cache-control': "no-cache",
    }

    conn.request("GET", "/sales/activity/ajax.php?act=aSetHoneyCenterUserInfo", headers=headers)

    res = conn.getresponse()
    data = res.read()

    print("[mafengwo_fengmi][time:{}][res:{}]".format(curr_now(), data))

def mafengwo_zhuanpan_sign_in():
    """马蜂窝蜂蜜转盘 ios 客户端签到"""
    conn = http.client.HTTPSConnection("m.mafengwo.cn")

    payload = "act=honeyTurntable&async=false&key=sales%3Aactivity%3Ahoney_center"

    headers = {
        'content-length': "66",
        'accept': "application/json, text/javascript, */*; q=0.01",
        'origin': "https://m.mafengwo.cn",
        'x-requested-with': "XMLHttpRequest",
        'user-agent': "Mozilla/5.0 (Linux; Android 6.0.1; Nexus 5 Build/M4B30Z; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/61.0.3163.98 Mobile Safari/537.36 mfwappcode/com.mfw.roadbook mfwappver/8.0.4 mfwversioncode/445 mfwsdk/20140507 channel/TengXun mfwjssdk/1.1 mfwappjsapi/1.2",
        'content-type': "application/x-www-form-urlencoded; charset=UTF-8",
        'referer': "https://m.mafengwo.cn/sales/activity/honey_center/",
        'accept-encoding': "gzip, deflate",
        'accept-language': "zh-CN,en-US;q=0.8",
        'cookie': '__idfa=00000000-0000-0000-0000-000000000000; __idfv=F6005B42-8F41-4C6F-80A4-6AD190FD3A7F; __openudid=F6005B42-8F41-4C6F-80A4-6AD190FD3A7F; PHPSESSID=82cf136e74qjc3rg79qlg5qh35; mfw_uid=9154997; __mfwlt=1509330923; __mfwlv=1509330923; __mfwvn=20; oad_n=a%3A3%3A%7Bs%3A3%3A%22oid%22%3Bi%3A2581%3Bs%3A2%3A%22dm%22%3Bs%3A16%3A%22mapi.mafengwo.cn%22%3Bs%3A2%3A%22ft%22%3Bs%3A19%3A%222017-10-25+22%3A21%3A00%22%3B%7D; UM_distinctid=15ec2f6c660146-00efefec2d986d-251f7468-3d10d-15ec2f6c662128; __mfwurd=a%3A3%3A%7Bs%3A6%3A%22f_time%22%3Bi%3A1506509504%3Bs%3A9%3A%22f_rdomain%22%3Bs%3A13%3A%22m.mafengwo.cn%22%3Bs%3A6%3A%22f_host%22%3Bs%3A1%3A%22m%22%3B%7D; __mfwuuid=59c7a7b7-5904-55f5-cbea-9460f64e4e15; uva=s%3A108%3A%22a%3A3%3A%7Bs%3A2%3A%22lt%22%3Bi%3A1506509504%3Bs%3A10%3A%22last_refer%22%3Bs%3A40%3A%22https%3A%2F%2Fm.mafengwo.cn%2Fsales%2F2217861.html%22%3Bs%3A5%3A%22rhost%22%3BN%3B%7D%22%3B; mfw_uuid=59c7a7b7-5904-55f5-cbea-9460f64e4e15',
        'cache-control': "no-cache",
    }

    conn.request("POST", "/sales/activity/ajax.php", payload, headers)

    res = conn.getresponse()
    data = res.read()

    print("[mafengwo_zhuanpan][time:{}][res:{}]".format(curr_now(), data))

def fliggy_sigin_in():
    """阿里旅行网页签到"""

    conn = http.client.HTTPSConnection("ffa.fliggy.com")

    headers = {
        'dnt': "1",
        'accept-encoding': "gzip, deflate, br",
        'accept-language': "zh-CN,zh;q=0.8,en-US;q=0.6,en;q=0.4",
        'user-agent': "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.113 Safari/537.36",
        'accept': "*/*",
        'referer': "https://www.fliggy.com/mytrip/?spm=181.7091613.191938.39.140f2ea5SmtANE",
        'authority': "ffa.fliggy.com",
        'cookie': "hng=CN%7Czh-CN%7CCNY%7C156; uc1=cart_m=0&cookie14=UoTcCDbeYacXvg%3D%3D&lng=zh_CN&cookie16=VFC%2FuZ9az08KUQ56dCrZDlbNdA%3D%3D&existShop=true&cookie21=Vq8l%2BKCLjhZM&tag=8&cookie15=URm48syIIVrSKA%3D%3D&pas=0; uc3=sg2=V32Qr6DJ1TF4tL4LLd9j2i2CL159T9HpyqGS1jHsKGE%3D&nk2=qiAkoSc8&id2=UoMyzEOwbMhK&vt3=F8dBzLBA5lWNqSUbnVE%3D&lg2=VT5L2FSpMGV7TQ%3D%3D; tracknick=%5Cu4E0A%5Cu9053%5Cu9752; _l_g_=Ug%3D%3D; ck1=; unb=129390726; lgc=%5Cu4E0A%5Cu9053%5Cu9752; cookie1=BqbiJw1u%2BhPvU%2FqsokBrIei8lU5vYBvYsRV9Bl%2Fs4vk%3D; login=true; cookie17=UoMyzEOwbMhK; cookie2=1e35418b9c8ee8e725c965c3549dac39; _nk_=%5Cu4E0A%5Cu9053%5Cu9752; t=527bbe3dd43099eae1134460e7f4ccee; uss=ACjg%2B1KIqjLu0CPylLk5ikdcGqAvQfCQycfyNGe9VARxQSarJ%2BDjNMbplA%3D%3D; skt=d2f5703c9ff4c717; _tb_token_=7a697bb3304eb; cna=9TkxEtVPm30CAbSZ2xAI6rET; isg=AoiIZwYzRUoMvamFPCL_zVQBWfBame0_cRFVmEI5S4P7HS2H50OXyg5f68OW",
        'cache-control': "no-cache"
    }

    conn.request("GET", "/json/checkinInfo.htm?_ksTS=1507947064019_591&callback=jsonp592&channel=522", headers=headers)

    res = conn.getresponse()
    data = res.read()

    print("[fliggy][time:{}][res:{}]".format(curr_now(), data.decode("utf-8")))

def qyer_helper_sign_in():
    """行程助手ios客户的签到"""

    conn = http.client.HTTPSConnection("m.qyer.com")

    headers = {
        'host': "m.qyer.com",
        'cookie': "_guid=e6249f6d-ace5-cc55-725d-716b4afefef7; init_refer=; new_session=1; new_uv=29; session_time=1507946370.232; __utma=253397513.2072125957.1482678099.1507871724.1507946370.28; __utmb=253397513.1.10.1507946370; __utmc=253397513; __utmt=1; __utmz=253397513.1482678099.1.1.utmcsr=(direct)|utmccn=(direct)|utmcmd=(none); cdb_auth=d338y0TTubO70bytOC8pwlbuJxrFGzp1pVabGUqNzMTQmb4yf3sdi53Cn7nBl2lcnZqLUDDibZdBZHYcJc%2FbF6ieppkA7g; als=0",
        'user-agent': "Mozilla/5.0 (iPhone; CPU iPhone OS 11_0_3 like Mac OS X) AppleWebKit/604.1.38 (KHTML, like Gecko) Mobile/15A432 Planer/2.8.6",
        'x-requested-with': "XMLHttpRequest",
        'cache-control': "no-cache",
    }

    conn.request("GET", "/plan/require/app/encourage.php?action=signin&fromdevice=2", headers=headers)

    res = conn.getresponse()
    data = res.read()

    print("[qyer_help][time:{}][res:{}]".format(curr_now(), data.decode("utf-8")))

def chexiang_sign_in():
    """车享家ios客户端灌水签到"""

    conn = http.client.HTTPSConnection("h.jia.chexiang.com")
    payload = "--compressed"
    headers = {
        'host': "h.jia.chexiang.com",
        'accept': "application/json, text/plain, */*",
        'x-requested-with': "XMLHttpRequest",
        'accept-language': "zh-cn",
        'content-type': "application/json;charset=utf-8",
        'origin': "https://h.jia.chexiang.com",
        'user-agent': "{  \"clientId\" : \"93c36ab85c994b04b184c3653297eaed\",  \"deviceId\" : \"723D3C53-952C-4FF2-8C80-EE0D47788F4B\",  \"appCode\" : \"MongoToC\",  \"plateformType\" : \"ios\",  \"signature\" : \"2009CFFC21D78FE8B8C0A0B1E5741ACF\",  \"origin\" : \"Mozilla\/5.0 (iPhone; CPU iPhone OS 11_0_3 like Mac OS X) AppleWebKit\/604.1.38 (KHTML, like Gecko) Mobile\/15A432\",  \"userToken\" : \"MTAwMDU5ZWNhNzg4NWE2MzRlODgxMDY1MjMwNSLkvLka68lia3_un5ki1aVctZjN\",  \"sourceCode\" : \"APPStore\",  \"deviceManufacturer\" : \"iPhone\",  \"appVersion\" : \"4.3.1\",  \"userAccount\" : \"17621856713\",  \"signVersion\" : \"0.2\"}",
        'referer': "https://h.jia.chexiang.com/cx/cxj/cxjweb/checkins/checkins.shtml?userInfo=JTdCJTIyc291cmNlVHlwZSUyMiUzQSUyMjIlMjIlMkMlMjJsb2NhbFglMjIlM0ElMjIxMjEuMzc3NDAxJTIyJTJDJTIybG9jYWxZJTIyJTNBJTIyMzEuMzI0Mzk4JTIyJTJDJTIybW9iaWxlUGhvbmUlMjIlM0ElMjIxNzYyMTg1NjcxMyUyMiUyQyUyMmNpdHlOYW1lJTIyJTNBJTIyJUU0JUI4JThBJUU2JUI1JUI3JUU1JUI4JTgyJTIyJTJDJTIydXNlcklkJTIyJTNBJTIyS0h5OTJnJTJGV2UxTXRYbTRBUWVmRld3JTNEJTNEJTIyJTJDJTIyZXF1SWQlMjIlM0ElMjI3MjNEM0M1My05NTJDLTRGRjItOEM4MC1FRTBENDc3ODhGNEIlMjIlMkMlMjJjdXN0TmFtZSUyMiUzQSUyMiUyMiU3RA==",
        'cookie': 'user_trace_cookie=CiCcDln3NDBJpVSRMEexAg==; analysis_sign=10652305; wemall_cxid_c=10652305; wemall_equid_c=723D3C53-952C-4FF2-8C80-EE0D47788F4B; wemall_openid_c=""; wemall_opentype_c=6; wemall_userkey_c=62882c7f-3644-46d1-ad1c-c8131d339161; _ga=GA1.2.1080391224.1509372664; _gid=GA1.2.879806854.1509372664; wcid=26D47ADB-80AD-4FAF-BD19-06952B0647E7',
        'cache-control': "no-cache",
    }
    conn.request("POST", "/water/addWater.htm", payload, headers)
    res = conn.getresponse()
    data = res.read()
    print("[chexiang][time:{}][res:{}]".format(curr_now(), data.decode("utf-8")))

if __name__ == '__main__':

    qyer_sign_in()
    smzdm_sign_in()
    music_163_sign_in()
    nuomi_sign_in()
    #gewara_sign_in()
    #ctrip_sign_in()
    jd_sign_in()
    baidumap_sign_in()
    umetrip_sign_in()
    xiami_sign_in()
    futunn_sign_in()
    mafengwo_fengmi_sign_in()
    mafengwo_zhuanpan_sign_in()
    # fliggy_sigin_in()
    qyer_helper_sign_in()
    chexiang_sign_in()

