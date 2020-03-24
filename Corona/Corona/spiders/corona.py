
import scrapy


class CoronaSpider(scrapy.Spider):
    name = 'corona'
#    allowed_domains = ['books.toscrape.com']
    start_urls = ['https://www.worldometers.info/coronavirus/']

    def parse(self, response):

        stats = response.xpath(".//table[@id='main_table_countries_today']")
        
        for stat in stats:
            cases = stat.xpath("//tbody[2]/tr[@class='total_row']/td[2]").extract_first()
            deaths = stat.xpath("//tbody[2]/tr[@class='total_row']/td[4]").extract_first()
            recovered = stat.xpath("//tbody[2]/tr[@class='total_row']/td[6]").extract_first()
            active = stat.xpath("//tbody[2]/tr[@class='total_row']/td[7]").extract_first()

            yield {
                'Cases': cases,
                'Deaths': deaths,
                'Recovered': recovered,
                'Active': active,
            }
