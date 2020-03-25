# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy
from scrapy.loader.processors import MapCompose, TakeFirst, Join
from w3lib.html import remove_tags

def remove_quotations(value):
        return value.replace(u"\u201d," '').replace(u"\u201c", '')

class CoronaItem(scrapy.Item):
    Cases= scrapy.Field(
        input_processor= MapCompose(remove_tags),
        output_processor= TakeFirst()
    )
    Deaths= scrapy.Field(
        input_processor= MapCompose(remove_tags),
        output_processor= TakeFirst()
    )
    Recovered= scrapy.Field(
        input_processor= MapCompose(remove_tags),
        output_processor = TakeFirst()
    )
    Active= scrapy.Field(
        input_processor= MapCompose(remove_tags),
        output_processor = TakeFirst()
    )

