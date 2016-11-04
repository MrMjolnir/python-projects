# -*- coding: utf-8 -*-
import scrapy
from sportscalendar.items import scItem


class CpSpider(scrapy.Spider):
    name = "cp"
    allowed_domains = ["carreraspopulares.com"]
    start_urls = (
        'http://www.carreraspopulares.com/calendario_carreras/WR_KK01_menu_carreras.asp?fr_tipo_cons=5&fr_id_deporte=1&fr_id_pais=10&fr_id_dias=30',
    )

    def parse(self, response):
        for carrera in response.xpath('//div[re:test(@class, "race")]'):
            item = scItem()
            item['nombre'] = carrera.xpath('div[2]/a/h3/text()').extract()[0]
            tipo = carrera.xpath('div[2]/p[3]/text()').extract()[0]
            # para sacar la url tengo que entrar en cada ficha... item['surl'] = tipo + "   " + carrera.xpath('td[7]/a/img/@title').extract()[0]
            item['surl'] = tipo
            item['sitio'] = carrera.xpath('div[2]/p[2]/text()').extract()[0]
            item['fecha'] = carrera.xpath('div[2]/p[1]/text()').extract()[0]
            # print fecha, nombre, tipo, surl
            yield item



