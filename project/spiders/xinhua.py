# -*- coding: utf-8 -*-

import scrapy

from project.items import TextItem


class XinhuaSpider(scrapy.Spider):
    name = "xinhua"
    allowed_domains = ["www.xinhuanet.com"]
    start_urls = [
        "http://www.xinhuanet.com/",
    ]

    def parse(self, response):
        for sel in response.xpath('//a'):
            item = TextItem()
            item['text'] = sel.xpath('text()').extract()
            yield item
