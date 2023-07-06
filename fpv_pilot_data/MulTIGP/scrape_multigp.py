#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat May 27 18:40:33 2023
@author: seanyoo
"""

import chromedriver_autoinstaller
from selenium import webdriver
from bs4 import BeautifulSoup
chromedriver_autoinstaller.install()
import pandas as pd


driver = webdriver.Chrome()
url = "https://www.multigp.com/2022-multigp-series-global-qualifier-leaderboard/"
driver.get(url)


# page2_button = driver.find_element('css selector', '.paginate_button:nth-child(5)')
# page2_button.click()

# Wait for the page to load after navigating
driver.implicitly_wait(5)



html = driver.page_source
soup = BeautifulSoup(html, 'html.parser')




odds = soup.find_all('tr', class_='pro odd')
evens = soup.find_all('tr', class_='pro even')




pilot_names = []
race_infos = []
chapter_names = []
links = []

# Extract the desired information from the row and append to the respective lists
for even in evens: 
    pilot_name = even.find('a').text.strip()
    race_info = even.find_all('a')[1].text.strip()[6:]
    chapter_name = even.find_all('a')[2].text.strip()
    link = "https://www.multigp.com" + even.find("a")["href"]

    pilot_names.append(pilot_name)
    race_infos.append(race_info)
    chapter_names.append(chapter_name)
    links.append(link)


for odd in odds: 
    pilot_name = odd.find('a').text.strip()
    race_info = odd.find_all('a')[1].text.strip()[6:]
    chapter_name = odd.find_all('a')[2].text.strip()
    link = "https://www.multigp.com" + odd.find("a")["href"]

    pilot_names.append(pilot_name)
    race_infos.append(race_info)
    chapter_names.append(chapter_name)
    links.append(link)





# Create a DataFrame using the lists
df = pd.DataFrame({
    'Pilot Name': pilot_names,
    'Race Info': race_infos,
    'Chapter Name': chapter_names,
    'Link': links
})

# Print the DataFrame
df.to_excel("racer0.xlsx")
print("done6")