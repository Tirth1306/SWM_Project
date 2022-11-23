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
driver.get('https://twitter.com/search?q=%23layoffs&src=typeahead_click')
time.sleep(10)

scroll_pause_time = 1 # You can set your own pause time. My laptop is a bit slow so I use 1 sec
screen_height = driver.execute_script("return window.screen.height;")   # get the screen height of the web
i = 1

def scroll(i):
    # scroll one screen height each time
    driver.execute_script("window.scrollTo(0, {screen_height}*{i});".format(screen_height=screen_height, i=i))  
    i += 1
    time.sleep(scroll_pause_time)
    # update scroll height each time after scrolled, as the scroll height can change after we scrolled the page
    # scroll_height = driver.execute_script("return document.body.scrollHeight;")  
    return i
    # Break the loop when the height we need to scroll to is larger than the total scroll height
    # if (screen_height) * i > scroll_height or i > 50:
    #     break 

# print(blocks.text)
while True:
    blocks = []
    blocks = driver.find_elements_by_css_selector('[data-testid="cellInnerDiv"]')
    tweet_texts = driver.find_elements_by_css_selector('[data-testid="subreddit-name"]')
    likes = driver.find_elements_by_css_selector('[data-testid="like"]')
    replies = driver.find_elements_by_css_selector('[data-testid="reply"]')
    retweets = driver.find_elements_by_css_selector('[data-testid="retweet"]')
    user_names = driver.find_elements_by_css_selector('[data-testid="User-Names"]')
    print(len(blocks), len(tweet_texts))
    
    for block in range(len(blocks)):
        temp = []
        print("num //////// ", block)
        print("tweet_texts",tweet_texts[block].text)
        print("likes",likes[block].text)
        print("replies",replies[block].text)
        print("retweets",retweets[block].text)
        # print("---",user_names[block].text,"---")
        print("---",user_names[block].text.split('\n')[0],"---")
        print("---",user_names[block].text.split('\n')[1],"---")
        print("---",user_names[block].text.split('\n')[-1],"---")

        temp.append(tweet_texts[block].text)
        temp.append(likes[block].text)
        temp.append(replies[block].text)
        temp.append(retweets[block].text)
        # print("---",user_names[block].text,"---")
        temp.append(user_names[block].text.split('\n')[0])
        temp.append(user_names[block].text.split('\n')[1])
        temp.append(user_names[block].text.split('\n')[-1])
        data.append(temp)
        print("==============")
    break
    # i = scroll(i)
    # print(i)
    
    # if (i>=5):
    #     break

df = pd.DataFrame(data, columns=['Tweet_Text','Likes','Replies','Retweets','Name', 'Username','Time'])
df.to_csv("sample_twitter_data.csv",index=False)
# driver.close()