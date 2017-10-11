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
        'cookie': "__utma=253397513.1667471721.1476627137.1486093623.1486177584.17; __utmb=253397513.1.10.1486177584; __utmc=253397513; __utmt=1; __utmz=253397513.1476627137.1.1.utmcsr=(direct)|utmccn=(direct)|utmcmd=(none); _guid=c50082bd-15a4-c693-dc03-24ffffdcfad0; init_refer=; new_session=1; new_uv=17; session_time=1486177583; cdb_auth=2fd7%2BuJDATGAZtUZ0sEocWnV6ZVZ79H5s14PpNFflLUhPiIP%2B6uVCZhQfqg1CEo2fqc3dWPe6fqcql919ot4FPqJEJd3fA; als=0",
        'user-agent': "QYER/7.4 (iPhone; iOS 10.2.1; Scale/2.00)",
    }

    conn.request("POST", "/qyer/mileage/sign/add_mileage", payload, headers)

    res = conn.getresponse()
    data = res.read()

    print("[qyer][time:{}][res:{}]".format(curr_now(), data.decode("utf-8")))

def smzdm_sign_in():

    """什么值得买客户端签到"""
    conn = http.client.HTTPSConnection("api.smzdm.com")

    payload = "f=iphone&sk=uiWkBkg57AMGgHLwyyG2m1qDxYhzQNRLBxZfKVS4%252BIx1%2FMNqprtg4BKecGkdxDTy&token=54537f7044811152704&v=5.0&weixin=1"

    headers = {
        'host': "api.smzdm.com",
        'content-type': "application/x-www-form-urlencoded",
        'cookie': "device_id=0ggWhPmKxHzTDvKF24YJ3y6Py1Qv9dNyjVHDEwazEAUN9a5RZWpvpQ==; device_name=iPhone 6s; device_push=notifications_are_disabled; device_s=4AV2/Xtutz19ebZ6LkBPT5PdjEzAF2arHXBblhuQMRuYGa4RMTPgI1zQhJe81ZkHz8fVBPKucw=; device_smzdm=iphone; device_smzdm_version=7.6; device_system_version=10.2.1; device_type=iPhone8,1; login=1; network=WiFi_Net; partner_id=0; partner_name=AppStore; sess=54537f7044811152704; smzdm_id=6418214012; __ckguid=lpi28Cg154wJ7N4VkL4H6N4; __jsluid=ab4c1ed89fd3fb715b47dd3f4f402848; __ckguid=ecu4hlnBgB7f1VftHOl3Co2; _ga=GA1.2.1848225762.1447993948; Hm_lvt_9b7ac3d38f30fe89ff0b8a0546904e58=1482416015; smzdm_user_source=AEF63FB28C36CAC0B5F09EC24FEEC252",
        'user-agent': "smzdm_iPhone/7.6 (iPhone; iOS 10.2.1; Scale/2.00)smzdmapp",
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
        'cookie': "MKT_Pagesource=H5; _jzqco=%7C%7C%7C%7C1489215185494%7C1.905210666.1455900703011.1489215216335.1489215229617.1489215216335.1489215229617.0.0.0.32.32; cticket=83B18B3D138789BD220EC796908422BAFAE5CCC3779EC87911823971FFE6EDBE; isNonUser=false; _n_cid=12021067210004192157; _abtest_userid=467b8ea3-4289-4840-978d-0ead9501dc78; _ga=GA1.2.499933121.1444525450; __zpspc=9.1.1444525449.1444525449.1%234%7C%7C%7C%7C%7C%23; _bfa=1.1444525448857.2mqlyq.1.1444525448857.1444525448857.1.1",
        'accept': "application/json",
        'user-agent': "Mozilla/5.0 (iPhone; CPU iPhone OS 10_2_1 like Mac OS X) AppleWebKit/537.51.1 (KHTML, like Gecko) Mobile/11B508_eb64__Ctrip_CtripWireless_7.1.2",
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
        'cookie': "BDUSS=XRBMzJBRUFIcnhEVGtwS1JOS3ZENERGQmcxN2ZYYkdVSHlKRGc1OTh4QWYyYWRZSVFBQUFBJCQAAAAAAAAAAAEAAAAf3ZwJt7nQobezAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAB9MgFgfTIBYQ; BAIDUID=1D43E5A7AB576D4D145FE1F0C0F0E710:FG=1; BIDUPSID=236E51D87EDDDBED261296F61F127CE5; PSTM=1450593054",
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
        'cache-control': "no-cache",
        'postman-token': "1abbe95f-0d9f-4b73-bd8e-9e7042f635c5"
    }

    conn.request("GET", "/site/sign-in", headers=headers)

    res = conn.getresponse()
    data = res.read()

    print("[futunn][time:{}][res:{}]".format(curr_now(), data.decode("utf-8")))


if __name__ == '__main__':

    qyer_sign_in()
    smzdm_sign_in()
    music_163_sign_in()
    nuomi_sign_in()
    gewara_sign_in()
    ctrip_sign_in()
    jd_sign_in()
    baidumap_sign_in()
    umetrip_sign_in()
    xiami_sign_in()
    futunn_sign_in()

