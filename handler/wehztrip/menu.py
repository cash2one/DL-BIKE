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
			   "name":"实时公交",
			   "key":"bus"
			},
			{
			   "type":"click",
			   "name":"搜索",
			   "key":"search"
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
			   "name":"摇号查询",
			   "key":"yaohao"
			},
			{
			   "type":"click",
			   "name":"领红包",
			   "key":"good"
			},
			{
			   "type":"click",
			   "name":"查停车位",
			   "key":"park"
			},
			{
			   "type":"click",
			   "name":"空气污染",
			   "key":"pm25"
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
# appsecret: cc1ef16876f29a2b6e745a962cea985e

conn.request("POST", "/cgi-bin/menu/create?access_token=TjxPmwAesSqbgUyK6R8K9vbqWbO4p_dot_YBYLekML0yChZU6sJlyO51y9D8ME6zRhfQO6ULHt7-5Lao9BU2kcZCVYXbVTITBqdov8HWmWZaTV2nQGmG1cqZ5R6HrGTsQRFiAAAUVJ", obj_menu.encode("utf8"))

res = conn.getresponse()
data = res.read()

print(data.decode("utf-8"))



