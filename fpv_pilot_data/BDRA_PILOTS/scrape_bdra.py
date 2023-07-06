#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jun 14 14:12:56 2023

@author: seanyoo
"""

import chromedriver_autoinstaller
from selenium import webdriver
from bs4 import BeautifulSoup
chromedriver_autoinstaller.install()
import pandas as pd


driver = webdriver.Chrome()
url = "https://www.ifpv.co.uk/2023-championship-table-full"
driver.get(url)


# Wait for the page to load after navigating
driver.implicitly_wait(5)



html = driver.page_source
soup = BeautifulSoup(html, 'html.parser')

evens = soup.find_all("tr", class_="odd")
odds = soup.find_all("tr", class_="even")

pilot_names = []
race_infos = []
chapter_names = []
links = []
scores = []

for even in evens: 
    draft = even.find("a")
    href = "https://www.ifpv.co.uk" + draft['href']
    pilot = draft.get_text()
    draft2 = even.find("td", class_="sorting_1")
    score = draft2.get_text().strip()
    scores.append(score)
    pilot_names.append(pilot)
    links.append(href)
    
    
for odd in odds: 
    draft = odd.find("a")
    href = "https://www.ifpv.co.uk" + draft['href']
    pilot = draft.get_text()
    draft2 = even.find("td", class_="sorting_1")
    score = draft2.get_text().strip()
    scores.append(score)
    pilot_names.append(pilot)
    links.append(href)
    

        
