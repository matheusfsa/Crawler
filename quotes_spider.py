import scrapy
def isreceita(rec):
    if rec.find("/receita"):
        return True
    else:
        return False
class QuotesSpider(scrapy.Spider):
    name = "pegareceitas"
    user_agent = "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/22.0.1207.1 Safari/537.1"
    start_urls = ['http://www.tudogostoso.com.br/categorias/1037-doces-e-sobremesas?page={}'.format(i+1) for i in range(120)]

    def parse(self, response):
        #text = [sel.xpath('//a/@href').extract() for sel in  response.xpath('//a') if isreceita(sel.xpath('//a/@href').extract())]
        #print(text)
        receitas = set()
        for sel in response.xpath('//a'):
            rec = sel.xpath('//a/@href').extract()

            for x in rec:
                if str(x).find('/receita')!=-1:
                    nr = "http://www.tudogostoso.com.br" + str(x)
                    if nr not in receitas:
                        receitas.add("http://www.tudogostoso.com.br" + str(x))
        #print("receitas:{}".format(receitas))
        filename = 'C:/Users/Familia Sa/tutorial/tutorial/receitas.txt'
        with open(filename, 'w') as f:
            for r in receitas:
                f.write(r + '\n')
            f.close()
        self.log('Saved file {}'.format(filename))

        #print(filter(isreceita, text))
        #res = [x for x in text if isreceita(x)]
        #print(res)
