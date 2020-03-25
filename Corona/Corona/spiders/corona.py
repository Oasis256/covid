import scrapy
from scrapy.loader import ItemLoader
from Corona.items import CoronaItem

class CoronaSpider(scrapy.Spider):
    name = 'corona'
#Request
    start_urls = ['https://www.worldometers.info/coronavirus/'
    ]
#Response
    def parse(self, response):
        for stat in response.xpath(".//table[@id='main_table_countries_today']"):
            loader=ItemLoader(item=CoronaItem(), selector=stat, response=response)
            loader.add_xpath('Cases',".//tbody[2]/tr[@class='total_row']/td[2]/text()")
            loader.add_xpath('Deaths',".//tbody[2]/tr[@class='total_row']/td[4]/text()")
            loader.add_xpath('Recovered',".//tbody[2]/tr[@class='total_row']/td[6]/text()")
            loader.add_xpath('Active',".//tbody[2]/tr[@class='total_row']/td[7]/text()")
            yield loader.load_item()




