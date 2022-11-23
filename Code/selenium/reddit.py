# to add capabilities for chrome and firefox, import their Options with different aliases
from selenium.webdriver.chrome.options import Options as CustomChromeOptions
from selenium.webdriver.chrome.service import Service as ChromeService
from seleniumwire import webdriver
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
driver.get('https://www.reddit.com/search/?q=layoffs')
time.sleep(10)

scroll_pause_time = 1 # You can set your own pause time. My laptop is a bit slow so I use 1 sec
screen_height = driver.execute_script("return window.screen.height;")   # get the screen height of the web
i = 1

while True:
    # scroll one screen height each time
    driver.execute_script("window.scrollTo(0, {screen_height}*{i});".format(screen_height=screen_height, i=i))  
    i += 1
    time.sleep(scroll_pause_time)
    # update scroll height each time after scrolled, as the scroll height can change after we scrolled the page
    scroll_height = driver.execute_script("return document.body.scrollHeight;")  
    
    # Break the loop when the height we need to scroll to is larger than the total scroll height
    if (screen_height) * i > scroll_height or i > 1:
        break 

time.sleep(10)


blocks = driver.find_elements_by_css_selector('[data-testid="post-container"]')
sub_reddit = driver.find_elements_by_css_selector('[data-testid="subreddit-name"]')
post_author = driver.find_elements_by_css_selector('[data-testid="post_author_link"]')
post_time = driver.find_elements_by_css_selector('[data-testid="post_timestamp"]')
interaction = driver.find_elements_by_class_name('_2IpBiHtzKzIxk2fKI4UOv1._2n04GrCyhhQf-Kshn7akmH.HNL__wz5plDpzJe5Lnn')
reddit_text = driver.find_elements_by_class_name('_2SdHzo12ISmrC8H86TgSCp._1zpZYP8cFNLfLDexPY65Y7')
print(len(blocks), len(reddit_text), len(post_author), len(sub_reddit),len(post_time))

for block in range(len(blocks)):
    temp = []

    print("sub_reddit",sub_reddit[block].text)
    print("post_author",post_author[block].text)
    print("post_time",post_time[block].text)
    print("reddit_text",reddit_text[block].text)
    # print("---",user_names[block].text,"---")
    print("---",interaction[block].text.split('\n')[0],"---")
    print("---",interaction[block].text.split('\n')[1],"---")
    print("---",interaction[block].text.split('\n')[-1],"---")

    temp.append(sub_reddit[block].text)
    temp.append(sub_reddit[block].get_attribute('href'))
    temp.append(post_author[block].text)
    temp.append(post_author[block].get_attribute('href'))
    temp.append(post_time[block].text)
    temp.append(reddit_text[block].text)
    temp.append(reddit_text[block].get_attribute('href'))

    temp.append(interaction[block].text.split('\n')[0])
    temp.append(interaction[block].text.split('\n')[1])
    temp.append(interaction[block].text.split('\n')[-1])
    data.append(temp)
    print("==============")
    

df = pd.DataFrame(data, columns=['sub_reddit','sub_reddit_link','post_author','post_author','post_time','reddit_text','reddit_link','upvotes', 'comments','awards'])
df.to_csv("sample_reddit_data.csv",index=False)
driver.close()