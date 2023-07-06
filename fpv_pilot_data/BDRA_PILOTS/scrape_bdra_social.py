#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jun 14 15:21:34 2023

@author: seanyoo
"""


import chromedriver_autoinstaller
from selenium import webdriver
from bs4 import BeautifulSoup

chromedriver_autoinstaller.install()
import pandas as pd
from scrape_link import links
from scrape_link import pilot_names
from scrape_link import scores

def get_social(links):
    instagram_links = []
    youtube_links = []
    
    for link in links:
        driver = webdriver.Chrome()
        url = link
        driver.get(url)
        driver.implicitly_wait(5)
        html = driver.page_source
        soup = BeautifulSoup(html, 'html.parser')
        
        div_elements = soup.find_all('div', class_='col-md-2 social-logo')
        
        try:
            youtube_link = ""
            instagram_link = ""
            
            for div_element in div_elements:
                anchor_tag = div_element.find('a')
                
                if anchor_tag:
                    href = anchor_tag['href']
                    
                    if 'youtube.com' in href:
                        youtube_link = href
                    elif 'instagram.com' in href:
                        instagram_link = href
            
            youtube_links.append(youtube_link)
            instagram_links.append(instagram_link)
            
        except:
            youtube_link = ""
            instagram_link = ""
            youtube_links.append(youtube_link)
            instagram_links.append(instagram_link)
        driver.quit()
    return(instagram_links, youtube_links)




instagram_links, youtube_links = get_social(links)



df = pd.DataFrame({
    'Pilot Name': pilot_names,
    'Score': scores,
    'Instagram': instagram_links,
    'Youtube': youtube_links
})

# Print the DataFrame
df.to_excel("info.xlsx")
print("done6")


