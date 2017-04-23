# coding=utf-8

# @Time    : 3/11/17 16:46
# @Author  : panda (panyuxin@moseeker.com)
# @File    : menu.py
# @DES     : 湘湖警点微信公众号


obj_menu = """{
      "button":[
		{
		   "name":"微办事",
		   "sub_button":[
			{
			   "type":"click",
			   "name":"身份证办理预约",
			   "key":"IDCardReservation"
			},
			{
			   "type":"click",
			   "name":"临时居住证预约",
			   "key":"residenceReservation"
			}]
       },
		{
		   "name":"微查询",
		   "sub_button":[
			{
			   "type":"click",
			   "name":"户口事项审批结果查询",
			   "key":"accountResultCheck"
			},
			{
			   "type":"click",
			   "name":"身份证制作完成情况查询",
			   "key":"IDCardResultCheck"
			}]
       },
	   {
		   "name":"微互动",
		   "sub_button":[
			{
			   "type":"click",
			   "name":"报警位置标注",
			   "key":"alarmPosition"
			},
			{
			   "type":"click",
			   "name":"线索提供",
			   "key":"clueProvide",
			},
			{
			   "type":"click",
			   "name":"意见建议",
			   "key":"suggestion",
			}]
       }]
 }
"""

import http.client

conn = http.client.HTTPSConnection("api.weixin.qq.com")

# hztrip
# appid: wx59d56a198f761599
# appsecret: 46dfb719a323bb66b32af93211c5385b

conn.request("POST", "/cgi-bin/menu/create?access_token=Jzmy4lTq5fP6Qo1YKGJQUvxSMhzRAFBg9ACnIcTzFQK3gJJrVt48MrpKIMNyP-h3m8CBd9kbrMc6aWiVi0A4RDEZ6L9SDcSNNxiXk4_RrhpZexvlNesQ7kukQ5Il6raVUQCdACANJV", obj_menu.encode("utf8"))

res = conn.getresponse()
data = res.read()

print(data.decode("utf-8"))



