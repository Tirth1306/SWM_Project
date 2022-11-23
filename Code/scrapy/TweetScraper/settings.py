USER_AGENT = 'TweetScraper'

# settings for spiders
BOT_NAME = 'TweetScraper'
LOG_LEVEL = 'INFO'

SPIDER_MODULES = ['TweetScraper.spiders']
NEWSPIDER_MODULE = 'TweetScraper.spiders'
ITEM_PIPELINES = {
    'TweetScraper.pipelines.SaveToFilePipeline':100,
}
# CONCURRENT_ITEMS = 200
# DEPTH_LIMIT = 10
CLOSESPIDER_ITEMCOUNT = 20
# CLOSESPIDER_TIMEOUT = 10
# DOWNLOAD_MAXSIZE = 100000
# CONCURRENT_REQUESTS = 32

SAVE_TWEET_PATH = './Data/tweet/'
SAVE_USER_PATH = './Data/user/'

DOWNLOAD_DELAY = 1.0

# settings for selenium
from shutil import which
SELENIUM_DRIVER_NAME = 'firefox'
SELENIUM_BROWSER_EXECUTABLE_PATH = which('firefox')
SELENIUM_DRIVER_EXECUTABLE_PATH = which('geckodriver')
SELENIUM_DRIVER_ARGUMENTS=['-headless']  
DOWNLOADER_MIDDLEWARES = {
    'scrapy_selenium.SeleniumMiddleware': 800
}
