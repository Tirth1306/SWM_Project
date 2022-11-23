import os, logging, json
from scrapy.utils.project import get_project_settings

from TweetScraper.items import Tweet, User
from TweetScraper.utils import mkdirs


logger = logging.getLogger(__name__)
SETTINGS = get_project_settings()

class SaveToFilePipeline(object):
    ''' pipeline that save data to disk '''

    def __init__(self):
        self.saveTweetPath = SETTINGS['SAVE_TWEET_PATH']
        self.saveUserPath = SETTINGS['SAVE_USER_PATH']
        mkdirs(self.saveTweetPath)
        mkdirs(self.saveUserPath)


    def process_item(self, item, spider):
        if isinstance(item, Tweet):
            savePath = os.path.join(self.saveTweetPath, item['id_'])
            if os.path.isfile(savePath):
                pass
            else:
                self.save_to_file(item,savePath)
                logger.debug("Add tweet:%s" %item['id_'])

        elif isinstance(item, User):
            savePath = os.path.join(self.saveUserPath, item['id_'])
            if os.path.isfile(savePath):
                pass
            else:
                self.save_to_file(item, savePath)
                logger.debug("Add user:%s" %item['id_'])

        else:
            logger.info("Item type is not recognized! type = %s" %type(item))


    def save_to_file(self, item, fname):
        with open(fname, 'w', encoding='utf-8') as f:
            json.dump(dict(item), f, ensure_ascii=False)
