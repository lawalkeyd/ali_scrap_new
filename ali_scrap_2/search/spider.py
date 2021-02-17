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