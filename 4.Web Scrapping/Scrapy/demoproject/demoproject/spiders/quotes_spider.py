import scrapy

class QuotesSpider(scrapy.Spider):
    name = 'quotes_spider'

    def start_requests(self):
        urls = ["https://quotes.toscrape.com/page/1/","https://quotes.toscrape.com/page/2/","https://quotes.toscrape.com/page/3/"]

        # Generator Function
        for url in urls:
            yield scrapy.Request(url=url,callback=self.parse)
    
    def parse(self,response):
        page_id = response.url.split("/")[-2]
        filename = "quotes-%s"%page_id

        with open(filename,"wb") as f:
            f.write(response.body)
        self.log('Saved File %s' %filename)
