#coding=utf-8
from selenium import webdriver
import os
from time import sleep

dr=webdriver.Chrome()
file_path='file:///'+os.path.abspath("switch_to_frame.html")
dr.get(file_path)

frs=dr.find_elements_by_tag_name('frame')
#进入第二个frame
dr.switch_to_frame(frs[1])
dr.find_element_by_id('kw1').send_keys('hello')
dr.find_element_by_id('su1').click()
sleep(2)
#进入最后一个frame
dr.switch_to_default_content()
dr.switch_to_frame(frs[-1])
sleep(2)
#进入第三个frame
dr.switch_to_default_content()
dr.switch_to_frame(frs[2])
dr.find_element_by_link_text(u'这是链接一').click()

sleep(2)

dr.quit()