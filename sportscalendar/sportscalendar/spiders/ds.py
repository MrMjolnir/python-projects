import scrapy
from sportscalendar.items import scItem

# Suiza 4:
# DS
# http://www.kikourou.net/resultats/
# https://livetrail.net/
# http://statistik.d-u-v.org/calendar.php
# hago carreraspopulares?

class DsSpider(scrapy.Spider):
    name = "ds"
    allowed_domains = ["datasport.com"]
    start_urls = {
        'https://www.datasport.com/en/calendar'
    }

    def parse(self, response):
        #   filename = response.url.split("/")[-2]
        #        with open(filename, 'wb') as f:
        #            f.write(response.body)
        for carrera in response.xpath('//tr[re:test(@class, "odd|even")]'):
            item = scItem()
            item['nombre'] = carrera.xpath('td[2]/a/text()').extract()[0]
            tipo = carrera.xpath('td[3]/text()').extract()[0]
            item['surl'] = tipo + "   " + carrera.xpath('td[7]/a/img/@title').extract()[0]
            item['sitio'] = carrera.xpath('td[15]/a/@href').re(r"q=(.*)")[0]
            item['fecha'] = carrera.xpath('td[1]/span/text()').extract()[0]
            # print fecha, nombre, tipo, surl
            yield item


# def parse_carreras(self, response):
#        for carrera_title in response.css('div.entries > ul > li a::text').extract():
#         yield {
#            'fecha': response.xpath('//tr[re:test(@class, "odd|even")]//span/text()').extract(),
#            'tipo': response.xpath('//tr[re:test(@class, "odd|even")]//td[3]/text()').extract(),
#            'id': xxx,
#            'surl': response.xpath('//tr[re:test(@class, "odd|even")]//img[contains(@src, "icon_website.gif")]/@title').extract()
#            #'urlcalendar': post_title,
#
#        }
