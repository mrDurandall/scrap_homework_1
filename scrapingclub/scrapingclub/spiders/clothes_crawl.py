import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule


class ClothesCrawlSpider(CrawlSpider):
    name = 'clothes_crawl'
    allowed_domains = ['scrapingclub.com']
    start_urls = ['https://scrapingclub.com/exercise/list_basic/']

    rules = (
        Rule(LinkExtractor(restrict_xpaths="//h4[@class='card-title']/a"), callback='parse_item', follow=True),
        Rule(LinkExtractor(restrict_xpaths="//a[contains(text(), 'Next')]"), follow=True),
    )

    def parse_item(self, response):
        item = {}
        item['title'] = response.xpath("//h3[@class='card-title']/text()").get()
        item['price'] = response.xpath("//div[@class='card-body']/h4/text()").get().lstrip('$')
        item['description'] = response.xpath("//p[@class='card-text']/text()").get()
        item['image'] = 'https://scrapingclub.com' + \
                        response.xpath("//img[contains(@class, 'card-img-top')]/@src").get()
        return item
