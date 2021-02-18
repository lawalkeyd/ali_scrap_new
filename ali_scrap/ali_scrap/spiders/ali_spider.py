import scrapy

class AliSpider(scrapy.Spider):
    name = 'ali'

    def __init__(self, *args, **kwargs):
        self.start_urls = ['https://www.alibaba.com/product-detail/Custom-UV-Long-sleeve-SPF-dry_62555868492.html?spm=a27aq.14005655.1_2.2.284932e8VRFOEz']

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