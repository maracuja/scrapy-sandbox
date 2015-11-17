import scrapy

from tutorial.items import TextItem


class BbcSpider(scrapy.Spider):
    name = "bbc"
    allowed_domains = ["bbc.co.uk"]
    start_urls = [
        "http://bbc.co.uk/news",
    ]

    def parse(self, response):
        for sel in response.xpath('//h3'):
            item = TextItem()
            item['text'] = sel.xpath('span/text()').extract()
            yield item
