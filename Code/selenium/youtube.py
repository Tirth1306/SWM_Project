from selenium.webdriver.chrome.options import Options as CustomChromeOptions
from selenium.webdriver.chrome.service import Service as ChromeService
from seleniumwire import webdriver
from selenium.webdriver.common.by import By 
from selenium.webdriver.support.ui import WebDriverWait 
from selenium.webdriver.support import expected_conditions as EC
# import webdriver for downloading respective driver for the browser
from webdriver_manager.chrome import ChromeDriverManager
import time
import pandas as pd

data = []
temp = []


def set_driver_for_browser(browser_name):
        """expects browser name and returns a driver instance"""
        # if browser is suppose to be chrome
        if browser_name.lower() == "chrome":
            chrome_options = webdriver.ChromeOptions()
            # automatically installs chromedriver and initialize it and returns the instance
            return webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=chrome_options)

driver = set_driver_for_browser("chrome")
driver.get('https://www.youtube.com/results?search_query=layoff')
time.sleep(10)

SCROLL_PAUSE_TIME = 5

driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

# Get scroll height
last_height = driver.execute_script("return document.body.scrollHeight")

while True:
    print("here")
    # Scroll down to bottom
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

    # Wait to load page
    time.sleep(SCROLL_PAUSE_TIME)

    # Calculate new scroll height and compare with last scroll height
    new_height = driver.execute_script("return document.body.scrollHeight")
    if new_height == last_height:
        print('hi')
        break
    last_height = new_height

user_data = driver.find_elements_by_xpath('//*[@id="dismissible"]')
heading = driver.find_elements_by_xpath('//*[@id="video-title"]')
metadata = driver.find_elements_by_xpath('//*[@id="metadata"]')
channel_name = driver.find_elements_by_xpath('//*[@id="channel-info"]')

for i in range(len(heading)):
    temp = []
    print("heading ===> ",heading[i].text)
    print("metadata ===> ", metadata[i].text) 
    print("metadata ===> ", metadata[i].text.split('\n')) 
    print("channel_name ===> ", channel_name[i].text)
    link = heading[i].get_attribute('href')
    temp.append(heading[i].text)
    temp.append(metadata[i].text.split('\n')[0])
    temp.append(metadata[i].text.split('\n')[1])
    temp.append(channel_name[i].text)
    temp.append(link)
    data.append(temp)

print(len(channel_name))

df = pd.DataFrame(data, columns=['Title','Views','Time','ChannelName','Link'])
df.to_csv("sample_youtube_data.csv",index=False)
driver.close()

