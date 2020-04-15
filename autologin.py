#!/usr/bin/env python
#coding=utf-8
import requests
 
url0='http://wlt.ustc.edu.cn/cgi-bin/ip'
cmd='set'
port=0 # port 0-8 对应 1-9 端口
time=0 # 连接时间自己换算为秒单位的数值，对应5个选项
# 永久：0，1小时：3600,4小时：14400，11小时：39600，14小时：50400

# 这里 username 和 passwd 换成自己的用户名和密码
values = {'name' : 'username',  'password' : 'passwd' }

# encode & headers
user_agent = 'Mozilla/4.0 (compatible; MSIE 5.5; Windows 10)'  
headers = { 'User-Agent' : user_agent }

# request
url = url0 + "?"+"cmd=set&url=URL&type="+str(port)+"&exp="+str(time)+"&go=+%BF%AA%CD%A8%CD%F8%C2%E7+"
reqGet = requests.post(url, data=values)
reqGet.encoding = reqGet.apparent_encoding
print (reqGet.text) 

