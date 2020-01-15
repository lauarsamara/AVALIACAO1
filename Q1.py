import scrapy

class TerraSpider(scrapy.Spider):

    name = 'Uol'
    start_urls = { 
        'https://www.uol.com.br/'
    }

    def parse(self,response):
        ###Valor cotação do dólar
        dolars = response.xpath ('//*[@id="HU_header"]/div[2]/div/div[2]/div[2]/ul/li[1]/a/span[2]/text()')
        print("Cotação Dolar:{}".format(len(dolars)))

        for dolar in dolars:
            conteudo = dolar.extract().strip()
            if conteudo !="":
                yield {
                    'Cotação do dolar': conteudo
                }