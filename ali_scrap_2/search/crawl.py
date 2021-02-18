from multiprocessing import Process
from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings
from .spider import AliSpider
from twisted.internet import reactor


class UrlCrawlerScript(Process):

    def __init__(self, spider):
        Process.__init__(self)
        settings = get_project_settings()
        self.crawler = CrawlerProcess(settings)
        self.crawler.install()
        self.crawler.configure()
        self.spider = spider

    def run(self, url):
        self.crawler.crawl(self.spider)
        self.crawler.start()
        reactor.run()


def url_crawl(url):
    spider = AliSpider(url)
    crawler = UrlCrawlerScript(spider)
    crawler.start()
    crawler.join()