# -*- coding: utf-8 -*-
import scrapy


url = 'http://www.loterias.caixa.gov.br/wps/portal/loterias/landing/megasena/!ut/p/a1/04_Sj9CPykssy0xPLMnMz0vMAfGjzOLNDH0MPAzcDbwMPI0sDBxNXAOMwrzCjA0sjIEKIoEKnN0dPUzMfQwMDEwsjAw8XZw8XMwtfQ0MPM2I02-AAzgaENIfrh-FqsQ9wNnUwNHfxcnSwBgIDUyhCvA5EawAjxsKckMjDDI9FQE-F4ca/dl5/d5/L2dBISEvZ0FBIS9nQSEh/pw/Z7_HGK818G0K8DBC0QPVN93KQ10G1/res/id=historicoHTML/c=cacheLevelPage/=/'


class SenacrawlerSpider(scrapy.Spider):
    name = 'SenaCrawler'
    allowed_domains = ['loterias.caixa.gov.br']
    start_urls = [url]

    def parse(self, response):
        for sel in response.xpath("/html/body/table/tbody/tr"):
            if not sel.xpath("./@bgcolor"):
                yield {
                    'concurso': sel.xpath("./td[1]/text()").get(),
                    'data_sorteio': sel.xpath("./td[3]/text()").get(),
                    'dez1': sel.xpath("./td[4]/text()").get(),
                    'dez2': sel.xpath("./td[5]/text()").get(),
                    'dez3': sel.xpath("./td[6]/text()").get(),
                    'dez4': sel.xpath("./td[7]/text()").get(),
                    'dez5': sel.xpath("./td[8]/text()").get(),
                    'dez6': sel.xpath("./td[9]/text()").get(),
                    'ganhadores_fx1': sel.xpath("./td[10]/text()").get(),
                    'ganhadores_fx2': sel.xpath("./td[11]/text()").get(),
                    'ganhadores_fx3': sel.xpath("./td[12]/text()").get(),
                    'valor_acumulado_prox_concurso': sel.xpath("./td[19]/text()").get(),
                    'acumulado': sel.xpath("./td[20]/text()").get()
                }




'''
    concurso = response.xpath("/html/body/table/tbody/tr/td[1]/text()").getall()
    data_sorteio = response.xpath("/html/body/table/tbody/tr/td[3]/text()").getall()
    dez1 = response.xpath("/html/body/table/tbody/tr/td[4]/text()").getall()
    dez2 = response.xpath("/html/body/table/tbody/tr/td[5]/text()").getall()
    dez3 = response.xpath("/html/body/table/tbody/tr/td[6]/text()").getall()
    dez4 = response.xpath("/html/body/table/tbody/tr/td[7]/text()").getall()
    dez5 = response.xpath("/html/body/table/tbody/tr/td[8]/text()").getall()
    dez6 = response.xpath("/html/body/table/tbody/tr/td[9]/text()").getall()
    ganhadores_fx1 = response.xpath("/html/body/table/tbody/tr/td[10]/text()").getall()
    ganhadores_fx2 = response.xpath("/html/body/table/tbody/tr/td[11]/text()").getall()
    ganhadores_fx3 = response.xpath("/html/body/table/tbody/tr/td[12]/text()").getall()
    rateio_fx1 = response.xpath("/html/body/table/tbody/tr/td[13]/text()").getall()
    rateio_fx2 = response.xpath("/html/body/table/tbody/tr/td[14]/text()").getall()
    rateio_fx3 = response.xpath("/html/body/table/tbody/tr/td[15]/text()").getall()

    valor_arrecadado = response.xpath("/html/body/table/tbody/tr/td[17]/text()").getall()
    estimativa_prox_concurso = response.xpath("/html/body/table/tbody/tr/td[18]/text()").getall()
    valor_acmulado_prox_concurso = response.xpath("/html/body/table/tbody/tr/td[19]/text()").getall()
    acumulado = response.xpath("/html/body/table/tbody/tr/td[20]/text()").getall()
    sorteio_especial = response.xpath("/html/body/table/tbody/tr/td[21]/text()").getall()
'''