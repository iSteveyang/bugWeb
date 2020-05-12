#coding=utf-8
import urllib2
import urllib
import re
import time
from random import choice
#代理ip地址list
iplist=['1.9.189.65:3128','27.24.158.130.80','27.24.158.154:80']
#要抓取的搜索关键字list
keywords=["书包","雨伞"]
for item in keywords:
	#随机选择代理ip地址
	ip=choice(iplist)
	word=urllib.quote(item)
	# url = "https://sug.so.360.cn/suggest?callback=suggest_so&encodein=utf-8&encodeout=utf-8&format=json&fields=word,obdata&word=" + word
	url = "http://yangkeduo.com/proxy/api/search_suggest?pdduid=0&query=" + word + "&plat=H5&source=index"
	headers={
			"GET":url,
			"Host": "yangkeduo.com",
			"Referer": "http://yangkeduo.com",
			"User_Agent":" Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:37.0) Gecko/20100101 Firefox/37.0"
		}
	#使用随机代理ip地址访问URL
	proxy_support=urllib2.ProxyHandler({'http':'http://'+ip})
	opener=urllib2.build_opener(proxy_support)
	urllib2.install_opener(opener)
	req=urllib2.Request(url)
	for key in headers:
		req.add_header(key,headers[key])
	html=urllib2.urlopen(req).read()
	#提取返回数据
	result=re.findall("\"(.*?)\"",html)
	#去掉集合中的一些无用数据
	r=('query','word','version','result','3.2.1','rec')
	for item in result:
		if item not in r:
			print (item)
	#抓取一次后休息3秒
		time.sleep(3)
