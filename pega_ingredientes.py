import scrapy


class QuotesSpider(scrapy.Spider):
    name = "pegaingredientes"
    user_agent = "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/22.0.1207.1 Safari/537.1"

    f = open("receitas.txt", 'r')
    text = f.read().split('\n')
    print(text)
    f.close()
    start_urls = [x for x in text if x != '']
    #start_urls = ['https://docs.scrapy.org/en/latest/topics/selectors.html#topics-selectors']
    def parse(self, response):

        titulo = response.css('div.recipe-title h1::text').extract()[0].replace('\n','')
        link = response.url
        ingredientes = response.css('span.p-ingredient::text').extract()
        t = (titulo,link, ingredientes)
        print(str(t))
        w = open('receitas_sobremesa.txt','a')
        w.write(str(t) + '\n')
        w.close()