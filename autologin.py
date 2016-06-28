#!/usr/bin/env python
#coding=utf-8
import urllib
import urllib2
 
url = 'http://wlt.ustc.edu.cn/cgi-bin/ip'
cmd='set'
port=0
time=0
values = {'name' : 'yourname',  'password' : 'yourpassword' }
user_agent = 'Mozilla/4.0 (compatible; MSIE 5.5; Windows 10)'  
headers = { 'User-Agent' : user_agent }  
data = urllib.urlencode(values)
geturl = url + "?"+"cmd=set&url=URL&type="+str(port)+"&time=0&go=+%BF%AA%CD%A8%CD%F8%C2%E7+"
request = urllib2.Request(geturl,data)
response = urllib2.urlopen(request)
print response.read()  
#request = urllib2.Request(url, data)  
#response = urllib2.urlopen(request)  
#page = response.read()
##the_page= unicode(page, "gbk").encode("utf8")
#print page   #print

