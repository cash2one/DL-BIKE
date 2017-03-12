# coding=utf-8

# @Time    : 3/11/17 16:46
# @Author  : panda (panyuxin@moseeker.com)
# @File    : menu.py
# @DES     :


obj_menu = """{
      "button":[
      {
		   "name":"查公交",
		   "sub_button":[
			{
			   "type":"click",
			   "name":"线路",
			   "key":"bus"
			},
			{
			   "type":"click",
			   "name":"站点",
			   "key":"station"
			},
			{
			   "type":"click",
			   "name":"周边",
			   "key":"around"
			},
			{
			   "type":"click",
			   "name":"换乘",
			   "key":"transfer"
			}]
       },
       {
		   "type":"click",
		   "name":"查自行车",
		   "key" :"bike"
       },
	   {
		   "name":"更多",
		   "sub_button":[
			{
			   "type":"click",
			   "name":"查停车位",
			   "key":"park"
			},
			{
			   "type":"view",
			   "name":"违章查询",
			   "url":"http://www.zjsgat.gov.cn:8080/was/phone/carIllegalQuery.jsp?zjolTitleName=%E8%BF%9D%E7%AB%A0%E6%9F%A5%E8%AF%A2"
			},
			{
			   "type":"click",
			   "name":"摇号查询",
			   "key":"yaohao"
			},
			{
			   "type":"click",
			   "name":"PM2.5",
			   "key":"pm25"
			},
			{
			   "type":"view",
			   "name":"打赏",
			   "url":"http://mp.weixin.qq.com/s?__biz=MjM5NzM0MTkyMA==&mid=208675856&idx=1&sn=92a8a58ef849c1d3e3909a6a3dd75af8#rd"
			}]
       }]
 }
"""

import http.client

conn = http.client.HTTPSConnection("api.weixin.qq.com")

conn.request("POST", "/cgi-bin/menu/create?access_token=0C5jnbKXZoMxs6mGj-Nd_AGZyi_VaMYKoJ8wH4IB08Lbd8recb5iiyz_DRKl0_J0lFXGt0hcREeMP3X9NpQwDoJ6GtQ14Sk4NDR8XSchK2z7UI4XuoRTQ-DwiNoljA_ubU-9ZfS07ihpn3w7_AE3kw", obj_menu)

res = conn.getresponse()
data = res.read()

print(data.decode("utf-8"))


