from multiprocessing import Process
from scrapy.crawler import CrawlerProcess
from scrapy.conf import settings
from ali_scrap.ali_scrap.spiders import ali_spider
from models import Domain
from ali_scrap.ali_scrap.spiders import ali_spider

class UrlCrawlerScript():

    def __init__(self):
        self.crawler = CrawlerProcess(settings)
        self.crawler.install()
        self.crawler.configure()

    def _crawl(self, url):
        start_urls = []
        start_urls.append(url)

        self.crawler.crawl(ali_spider(start_urls))
        self.crawler.start()
        self.crawler.stop()

    def crawl(self, url):
        p = Process(target=self._crawl, args=[url])
        p.start()
        p.join()

crawler = UrlCrawlerScript()

def url_crawl(url):
    crawler.crawl(url)