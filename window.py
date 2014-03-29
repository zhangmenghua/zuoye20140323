#coding=utf-8
from selenium import webdriver
import os
from time import sleep

dr=webdriver.Chrome()
file_path='file:///'+os.path.abspath("window.html")
dr.get(file_path)
sleep(3)

element1=dr.find_element_by_link_text(u'这是链接一')
url1=element1.get_attribute('href')

dr.get(url1)
sleep(3)
dr.quit()





