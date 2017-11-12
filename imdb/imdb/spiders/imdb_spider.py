# -*- coding: utf-8 -*-
import scrapy
import re
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from imdb.items import ImdbItem
 
 
class IMDBSpider(CrawlSpider):
    name = 'imdb'
    allowed_domains = ['imdb.com']
    start_urls = ['http://www.imdb.com/chart/top/?ref_=nv_mv_250_6']
 
   

    def parse(self, response):
        for sel in response.xpath("//*[contains(@class,'chart full-width')]/tbody/tr"):
            item = ImdbItem()
            item['titulo'] = sel.xpath('td[2]/a/text()').extract()[0].strip()
            item['puntuacionIMDB'] = sel.xpath('td[3]/strong/text()').extract()[0].strip()
            item['ranking'] = re.match(r'(^[0-9]+)',sel.xpath('td[2]/text()').extract()[0].__str__().strip()).group(1)
            item['anyoEstreno'] = sel.xpath('normalize-space(td[2]/span/text())').extract()[0].strip()
            item['enlace'] = "http://imdb.com"+sel.xpath('td[2]/a/@href').extract()[0]
            request = scrapy.Request(item['enlace'], callback=self.parsearInfoPelicula)
            request.meta['item'] = item
            yield request


    def parsearInfoPelicula(self, response):
        item = response.meta['item']
        item['director'] = response.xpath("//div/span[@itemprop='director']/a/span/text()").extract()
        item['guionistas'] = response.xpath("//div/span[@itemprop='creator']/a/span/text()").extract()
        item['sinopsis'] = response.xpath("normalize-space(//div[@itemprop='description']/text())").extract()[0]
        item['generos'] = response.xpath("//div[@itemprop='genre']/a/text()").extract()
        item['duracion'] = response.xpath("normalize-space(//div[@class='subtext']/time[@itemprop='duration']/text())").extract()[0]		
        return item
