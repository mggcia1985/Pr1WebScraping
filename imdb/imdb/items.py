# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class ImdbItem(scrapy.Item):
    # define the fields for your item here like:
    ranking = scrapy.Field()
    titulo = scrapy.Field()
    anyoEstreno = scrapy.Field()
    puntuacionIMDB = scrapy.Field()
    director = scrapy.Field()
    guionistas = scrapy.Field()
    duracion = scrapy.Field()
    sinopsis = scrapy.Field()
    generos = scrapy.Field()
    enlace = scrapy.Field()
