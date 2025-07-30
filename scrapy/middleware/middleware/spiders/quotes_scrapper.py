import scrapy
from middleware.items import QuoteItem


class QuotesScrapperSpider(scrapy.Spider):
    name = "quotes_scrapper"
    allowed_domains = ["quotes.toscrape.com"]
    start_urls = ["https://quotes.toscrape.com/"]

    def parse(self, response):
        for quote in response.css("div.quote"):
            item = QuoteItem()
            item["text"] = quote.css("span.text::text").get()
            item["author"] = quote.css("span small.author::text").get()
            item["tags"] = quote.css("div.tags a.tag::text").getall()
            yield item
