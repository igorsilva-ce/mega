# -*- coding: utf-8 -*-
import scrapy


url = "http://www.loterias.caixa.gov.br/wps/portal/loterias/landing/megasena/!ut/p/a1/04_Sj9CPykssy0xPLMnMz0vMAfGjzOLNDH0MPAzcDbwMPI0sDBxNXAOMwrzCjA0sjIEKIoEKnN0dPUzMfQwMDEwsjAw8XZw8XMwtfQ0MPM2I02-AAzgaENIfrh-FqsQ9wNnUwNHfxcnSwBgIDUyhCvA5EawAjxsKckMjDDI9FQE-F4ca/dl5/d5/L2dBISEvZ0FBIS9nQSEh/pw/Z7_HGK818G0K8DBC0QPVN93KQ10G1/res/id=historicoHTML/c=cacheLevelPage/=/"
response.xpath('//title/text()').get()


class SenacrawlerSpider(scrapy.Spider):
    name = 'SenaCrawler'
    allowed_domains = ['loterias.caixa.gov.br']
    start_urls = [url]

    def parse(self, response):
        response.xpath("/html/body/table/tbody[2]/tr[2]/td[1]/").getall()

        response.css("body > table:nth-child(1) > tbody:nth-child(2) > tr:nth-child(40) > td:nth-child(1)")

        response.xpath("/html/body/table/tbody[2]/tr[2]/td[1]/text()").get()



