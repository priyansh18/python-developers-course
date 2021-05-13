import scrapy



class QuotesSpider1(scrapy.Spider):
    name = 'quotes_spider1'

    def start_requests(self):
        urls = ["https://quotes.toscrape.com/page/1/","https://quotes.toscrape.com/page/2/","https://quotes.toscrape.com/page/3/"]
        for url in urls:
            yield scrapy.Request(url,callback=self.parse)

    def parse(self,response):
        page_id = response.url.split("/")[-2]
        filename = "quotes-%s"%page_id

        for q in response.css("div.quote"):
            text = q.css("span.text::text").get()
            author = q.css("small.author::text").get()
            tags = q.css("a.tag::text").getall()

            yield{
                'text':text,
                'author':author,
                'tags':tags,
            }

