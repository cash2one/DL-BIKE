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
			   "name":"搜索",
			   "key":"search"
			},
			{
			   "type":"click",
			   "name":"实时公交",
			   "key":"bus"
			},
			{
			   "type":"click",
			   "name":"电子站牌",
			   "key":"stop"
			},
			{
			   "type":"click",
			   "name":"附近",
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
			   "type":"click",
			   "name":"摇号查询",
			   "key":"yaohao"
			},
			{
			   "type":"click",
			   "name":"空气污染",
			   "key":"pm25"
			},
			{
			   "type":"view",
			   "name":"赞助",
			   "url":"https://mp.weixin.qq.com/s/Wm3HR2mgVXrqxQkKTv5c-w"
			},
			{
			   "type":"click",
			   "name":"联系我们",
			   "key":"contact"
			}]
       }]
 }
"""

import http.client

conn = http.client.HTTPSConnection("api.weixin.qq.com")

# hztrip
# appid: wx59d56a198f761599
# appsecret: 46dfb719a323bb66b32af93211c5385b

conn.request("POST", "/cgi-bin/menu/create?access_token=lKAaBT9k2N9eOrST0H1MQNJ2W0LmZxJ8kXNq_C_qUEg7gsw3aiBCee6Z026U8YVdqj2JS5YpCHKmox_52OZgcldQQeIspQNYwhee_zyAGzhXgSWBKIJF0kR7n0f8mDfaLQKaABAHMG", obj_menu.encode("utf8"))

res = conn.getresponse()
data = res.read()

print(data.decode("utf-8"))



