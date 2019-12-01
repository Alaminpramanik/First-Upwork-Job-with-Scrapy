# -*- coding: utf-8 -*-
import scrapy
from ..items import TheidlemanItem

class TheidlemanSpiderSpider(scrapy.Spider):
    name = 'theidleman'
    #allowed_domains = ['theidleman.com']
    start_urls = [
        'https://theidleman.com/collections/l-a-bruket'
    ]

    def parse(self, response):
        items=TheidlemanItem()

        product_url=response.css('.product-card a::attr(href)').extract()
        product_name=response.css('.bc-sf-filter-product-item-title::text').extract()
        brand_name=response.css('.bc-sf-filter-product-item-vendor::text').extract()

        items['product_url']=product_url
        items['product_name']=product_name
        items['brand_name']=brand_name

        yield items

