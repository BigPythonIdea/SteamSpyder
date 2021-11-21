# -*- coding: utf-8 -*-
"""
Created on Sat Nov 20 23:20:53 2021

@author: Mooncat
"""

# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
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
search = driver.find_element_by_xpath('/html/body/div[1]/div[7]/div[5]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[2]/div/div[9]/div[1]/form/div/input')
search.send_keys('艾爾登法環')
button1 = driver.find_element_by_xpath('/html/body/div[1]/div[7]/div[5]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[2]/div/div[9]/div[1]/form/div/a/img').click()
button2 = driver.find_element_by_xpath('/html/body/div[1]/div[7]/div[5]/form/div[1]/div/div[1]/div[3]/div[2]/div[3]/a[1]').click()



