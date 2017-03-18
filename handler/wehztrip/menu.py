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

conn.request("POST", "/cgi-bin/menu/create?access_token=oRgd35uZMRQbxlr-6S5HsH7mR4GhwPvAY2HF48GP_TJcKd88CV5Bon44faEbrcwiw2wiXt_fNwHu2-7Uslo0zlleMJoCgG-DtLFRTAHA13o-uOvyjbrhFXim_5Ik2AHBEAAbADATPP", obj_menu.encode("utf8"))

res = conn.getresponse()
data = res.read()

print(data.decode("utf-8"))



