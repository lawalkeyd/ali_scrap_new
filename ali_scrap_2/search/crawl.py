from multiprocessing import Process
from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings
from .spider import AliSpider

settings = get_project_settings()

class UrlCrawlerScript():

    def __init__(self):
        self.crawler = CrawlerProcess(settings)
        self.crawler.install()
        self.crawler.configure()

    def _crawl(self, url):
        self.crawler.crawl(AliSpider(url))
        self.crawler.start()
        self.crawler.stop()

    def crawl(self, url):
        p = Process(target=self._crawl, args=[url])
        p.start()
        p.join()

crawler = UrlCrawlerScript()

def url_crawl(url):
    crawler.crawl(url)