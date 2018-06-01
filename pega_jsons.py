import scrapy


class QuotesSpider(scrapy.Spider):
    name = "teste"
    user_agent = "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/22.0.1207.1 Safari/537.1"
    #start_urls = ['https://mdemulher.abril.com.br/receitas/busca/?tipo=biscoito-e-bolacha,bolinho-e-cupcake,bolo-com-recheio,bolo-simples,doce-caseiro,docinho-e-salgadinho,musse,pave,pudim,sorvete,sufle,torta-doce']
    start_urls = [
        'https://mdemulher.abril.com.br/filtros_receitas/?tipo=doce-caseiro,docinho-e-salgadinho,musse,pudim,sorvete,sufle,torta-doce&marca=claudia&pagina={}'.format(i+1) for i in range(4,90)]

    def parse(self, response):
        with open("jsons.txt", 'ab') as f:
            f.write(response.body)
