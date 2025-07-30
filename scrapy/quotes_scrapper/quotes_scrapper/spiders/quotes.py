import scrapy


class QuotesSpider(scrapy.Spider):
    name = "quotes"
    allowed_domains = ["quotes.toscrape.com"]
    start_urls = ["https://quotes.toscrape.com"]

    def parse(self, response):
        # explore response objects
        print('Response: ', response)
        print('Response Status: ', response.status)
        print('Response Headers: ', response.headers)
        
        #view page content
        print('Response Content: ', response.text[:500])
        
        # extract the title of the page
        page_title = response.css('title::text').get()
        print('Page Title: ', page_title)
        
        # 6/7/8. Extract all quotes, authors and tags from the page:
        quotes = response.css('div.quote')
        for quote in quotes:
            text = quote.css('span.text::text').get()
            author = quote.css('small.author::text').get()
            tags = quote.css('div.tags a.tag::text').getall()
            yield {
                'text': text,
                'author': author,
                'tags': tags
            }

        # 9. Navigate to the next page link:
        next_page = response.css('li.next a::attr(href)').get()
        if next_page:
            yield response.follow(next_page, callback=self.parse)
        
