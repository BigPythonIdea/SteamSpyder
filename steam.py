# -*- coding: utf-8 -*-
"""
Created on Sat Nov 20 23:20:53 2021

@author: Mooncat
"""

# -*- coding: utf-8 -*-
"""
常用指令
driver.find_element_by_xpath
.click()

格式
('/html/body/~~~')
"""

import pandas as pd
import time
import os
from threading import Thread

from selenium import webdriver
from selenium.webdriver.support.ui import Select

# Forza Horizon 5
# DEATH STRANDING
# Age of Empires IV

driver = webdriver.Firefox()
driver.get("https://store.steampowered.com/")
bnt = driver.find_element_by_xpath('/html/body/div[1]/div[7]/div[5]/div[1]/div[2]/div[16]/div/div[1]/div[2]/div[1]/div/a/span').click()


def get(*args):
    click_on = driver.find_element_by_xpath(args[0]).click()
    c = 1
    while(True):
        try:
            _ = driver.find_element_by_xpath('/html/body/div[1]/div[7]/div[5]/div[1]/div[3]/div[1]/div[5]/div[2]/div[1]/div['+str(c)+']/div/h1')
            c += 1
        except:
            break
    for i in range(1, c):
        game = driver.find_element_by_xpath('/html/body/div[1]/div[7]/div[5]/div[1]/div[3]/div[1]/div[5]/div[2]/div[1]/div['+str(i)+']/div/h1')
        price = driver.find_element_by_xpath('/html/body/div[1]/div[7]/div[5]/div[1]/div[3]/div[1]/div[5]/div[2]/div[1]/div['+str(i)+']/div/div[2]/div/div[1]')
        
    off = driver.find_element_by_xpath('/html/body/div[1]/div[7]/div[5]/div[1]/div[3]/div[1]/div[5]/div[2]/div[1]/div['+str(c-1)+']/div/div[2]/div[2]/div[1]/div[1]')
    yourprice = driver.find_element_by_xpath('/html/body/div[1]/div[7]/div[5]/div[1]/div[3]/div[1]/div[5]/div[2]/div[1]/div['+str(c-1)+']/div/div[2]/div[2]/div[1]/div[2]/div/div[2]')
    print(off.text)
    print(yourprice.text)
    
        

get('/html/body/div[1]/div[7]/div[5]/div[1]/div[4]/div/div/div[1]/div/a[1]/div[1]/img')


    
    


