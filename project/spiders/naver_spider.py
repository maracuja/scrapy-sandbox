# -*- coding: utf-8 -*-

import scrapy

from project.items import TextItem


class NaverSpider(scrapy.Spider):
    name = "naver"
    allowed_domains = ["news.naver.com"]
    start_urls = [
        "http://news.naver.com/",
    ]

    def parse(self, response):
        for sel in response.xpath('//a'):
            item = TextItem()
            item['text'] = sel.xpath('strong/text()').extract()
            yield item
