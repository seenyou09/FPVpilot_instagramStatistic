
import chromedriver_autoinstaller
from selenium import webdriver
from bs4 import BeautifulSoup
chromedriver_autoinstaller.install()
import pandas as pd



team_links = ["https://dcl.aero/team/alpha-prop-racing/", "https://dcl.aero/team/china-dragons/", "https://dcl.aero/team/cyclone-drone-racing/", "https://dcl.aero/team/dcl-wild-card-team/", "https://dcl.aero/team/haven-airborne/", "https://dcl.aero/team/mach1/", "https://dcl.aero/team/quad-force-one/", "https://dcl.aero/team/raiden-racing/","https://dcl.aero/team/sdt-perpetuumcoin/", "https://dcl.aero/team/xblades/"]



all_pilots = []
def get_social(team_website):
    for website in team_website:
        driver = webdriver.Chrome()
        url = website
        driver.get(url)
        
        
        # Wait for the page to load after navigating
        driver.implicitly_wait(5)
        
        
        
        html = driver.page_source
        soup = BeautifulSoup(html, 'html.parser')
        
        
        
        
        pilot_contents = soup.find_all("div", class_="pilot-details bg-navy align-left brand brand-small brand-right brand-green")
        
        for content in pilot_contents:
            pilot = []
            h4_tag = content.find("h4")
            handle = h4_tag.text
            h5_tag = content.find("h5")
            name = h5_tag.text
            pilot.append(handle)
            pilot.append(name)
        
            try:
                social_media = content.find("div", class_="pilot-socials social-media")
                tag1 = social_media.find("li", class_="instagram")
                tag2 = tag1.find("a")
                insta_link = tag2["href"]
                pilot.append(insta_link)
            except:
                insta_link =""
                pilot.append(insta_link)
            try:
                tag3 = social_media.find("li", class_="facebook")
                tag4 = tag3.find("a")
                facebook_link = tag4["href"]
                pilot.append(facebook_link)
            except:
                facebook_link =""
                pilot.append(facebook_link)
            try:
                tag5 = social_media.find("li", class_="youtube")
                tag6 = tag5.find("a")
                youtube_link= tag6["href"]
                pilot.append(youtube_link)
            except:
                youtube_link =""
                pilot.append(youtube_link)
            all_pilots.append(pilot)
    return(all_pilots)


pilot_social = get_social(team_links)

columns = ['Handle', 'Name', 'Instagram', 'Facebook', 'Youtube']

# Create a DataFrame from the pilot_social list
df = pd.DataFrame(pilot_social, columns=columns)

# Print the DataFrame
df.to_excel("DCL.xlsx")