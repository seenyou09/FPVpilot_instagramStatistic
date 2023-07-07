import pandas as pd
from bs4 import BeautifulSoup
import requests
import json
import re

class insta_stats:
    def __init__(self, insta_url):
        self.insta_url = insta_url
        self.existing_df = None
    
    def get_insta_info(self):
        response = requests.get(self.insta_url)
        soup = BeautifulSoup(response.text, "html.parser")
        info_dict = {'url': self.insta_url}
    
        # Get the name of the Instagram account
        try:
            name_element = soup.find('meta', property="og:title")
            name_content = name_element.get('content')
            name_content = name_content.split(")", 1)[0]
            name_content = name_content.split("(@", 1)[1]
            info_dict['name'] = name_content
        except:
            info_dict['name'] = ""
            
        # Get the follower, following, and post count of the account
        meta_tag = soup.find('meta', attrs={'property': 'og:description'})
        try:
            description = meta_tag.get('content')
        except:
            description = ""
        try:
            numbers = re.findall(r'\d{1,3}(?:,\d{3})*', description)
            numbers = [int(num.replace(',', '')) for num in numbers]
            info_dict['follower_count'] = numbers[0]
            info_dict['following_count'] = numbers[1]
            info_dict['post_count'] = numbers[2]
        except:
            info_dict['follower_count'] = 0
            info_dict['following_count'] = 0
            info_dict['post_count'] = 0
            
        # Get the account description
        descrp_tag = soup.find('script', type="application/ld+json")
    
        try:
            json_data = descrp_tag.contents[0]
            descrp_data = json.loads(json_data)
            description = descrp_data.get('description')
            clean_description = description.encode('utf-8').decode('unicode-escape').strip()
            info_dict['description'] = clean_description
        except:
            info_dict['description'] = ""
        
        return info_dict
    
    def updateJson(self, filename):
        entry = self.get_insta_info()
        try:
            with open(filename, "r") as file:
                data = json.load(file)
        except FileNotFoundError:
            data = {}
        
        key = entry["url"]
        data[key] = entry
        
        with open(filename, "w") as file:
            json.dump(data, file, indent= 4)

if __name__ == '__main__':
    filename = "insta_info.json"
    url = "https://www.instagram.com/zee.rover/"
    trial = insta_stats(url)
    yes = trial.updateJson(filename)
    print(yes)
