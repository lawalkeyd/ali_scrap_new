from multiprocessing import Process
from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings
from twisted.internet import reactor
import scrapy

class AliSpider(scrapy.Spider):
    name = 'ali'

    def __init__(self, *args, **kwargs):
        self.url = kwargs.get('url')
        self.start_urls = [self.url]

        super(AliSpider, self).__init__(*args, **kwargs)

    def parse(self, response):
        title = response.css('.module-pdp-title ::text').extract()
        images = response.css('.main-image-thumb-ul img::attr(src)').extract()
        price = response.css('.ma-ref-price span::text').extract()
        types = response.css('.sku-attr-val span::text').extract()        
        i = {}
        i['url'] = response.url
        i['title'] = title
        i['images'] = images
        i['price'] = price
        i['types'] = types
        return i

class UrlCrawlerScript():

    def __init__(self):
        Process.__init__(self)
        settings = get_project_settings()
        self.crawler = CrawlerProcess(settings)
        self.spider = AliSpider

    def run(self, url):
        self.crawler.crawl(self.spider, url=url)
        self.crawler.start()
        self.crawler.stop()

    def crawl(self, url):
        p = Process(target=self.run, args=[url])
        p.start()
        p.join()

def url_crawl(url):
    crawler = UrlCrawlerScript()
    crawler.crawl(url)

if __name__ == '__main__':
    print(url_crawl('https://www.alibaba.com/product-detail/Cocoon-Fishing-Performance-Hoodie-sublimated-hooded_62531342806.html?spm=a2700.details.deiletai6.8.73c21ae88f7OM0'))    