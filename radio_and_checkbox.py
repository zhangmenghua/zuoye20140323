#coding=utf-8
from selenium import webdriver
import os
import random
from time import sleep

input=raw_input('plese input radio or checkbox:')
n=int(raw_input('plese input int:'))
def random_select(what,count):
	if what=='radio':
		radios=dr.find_elements_by_css_selector('input[type=radio]')
		count_radio=len(dr.find_elements_by_css_selector('input[type=radio]'))
		if count>0 and count <=count_radio:
			radios[count-1].click()
		else:
			radios[count_radio-1].click()
		
	if what=='checkbox':
		checkboxs=dr.find_elements_by_css_selector('input[type=checkbox]')
		count_checkbox=len(dr.find_elements_by_css_selector('input[type=checkbox]'))
		if count>0 and count <=count_checkbox:
			list=random.sample(checkboxs,count)
			for checkbox in list:
				checkbox.click()
		else:
			for checkbox in checkboxs:
				checkbox.click()
	
dr=webdriver.Chrome()
file_path='file:///'+os.path.abspath('radio_and_checkbox.html')
dr.get(file_path)
random_select(input,n)
sleep(3)
dr.quit()