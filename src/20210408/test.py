#!/usr/bin/env python
# -*- coding:utf-8-*-
from selenium import webdriver

driver = webdriver.Chrome()
driver.get('sample.html')

for max_num_comment in driver.find_elements_by_xpath("//tbody/tr/td"):
    max_num = max_num_comment.text
    max_num = max_num.replace(" ", "")
    print("----------------------")
    print(max_num_comment)#text
    print("----------------------")