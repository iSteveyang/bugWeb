# coding:utf-8
from selenium import webdriver
import time
driver = webdriver.Firefox()
driver.implicitly_wait(10)
driver.get("http://www.baidu.com")
time.sleep(1)
driver.find_element_by_id("kw").send_keys(u"博客")
# 获取百度输入框的
time.sleep(1)
bd = driver.find_elements_by_class_name("bdsug-overflow")
for i in bd:
    print (i.get_attribute("data-key"))