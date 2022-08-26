import scrapy
from scrapy_splash import SplashRequest


class SplashClothSpider(scrapy.Spider):
    name = 'splash_cloth'
    allowed_domains = ['scrapingclub.com']
    # start_urls = ['http://scrapingclub.com/exercise/detail_sign/']

    script = '''        
        function main(splash, args)
          assert(splash:go(args.url))
          assert(splash:wait(0.5))
          return {
            html = splash:html(),
            png = splash:png(),
            har = splash:har(),
          }
        end
    '''

    def start_requests(self):
        yield SplashRequest(
            url='https://scrapingclub.com/exercise/detail_sign/',
            callback=self.parse,
            endpoint='execute',
            args={
                'lua_source': self.script
            }
        )

    def parse(self, response):
        item = {}
        item['title'] = response.xpath(".//h4[@class='card-title']/text()").get()
        item['price'] = response.xpath(".//h4[@class='card-price']/text()").get().lstrip('$')
        item['description'] = response.xpath(".//p[@class='card-description']/text()").get()
        item['image'] = response.urljoin(response.xpath(".//img[contains(@class, 'card-img-top')]/@src").get())
        yield item
