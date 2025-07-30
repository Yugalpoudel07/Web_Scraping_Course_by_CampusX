import scrapy
import json
from handling_apis.items import APIScraperItem

class PostsScraperSpider(scrapy.Spider):
    name = "posts_scraper"
    allowed_domains = ["jsonplaceholder.typicode.com"]
    #start_urls = ["https://jsonplaceholder.typicode.com/posts"]

    def start_requests(self):
        yield scrapy.Request(
            url = 'https://jsonplaceholder.typicode.com/posts',
            headers = {'User-Agent': 'Mozilla/5.0'},
            callback = self.parse
        )

    

    def parse(self, response):
        try:
            data = json.loads(response.text)
        except json.JSONDecodeError as e:
            self.logger.error(f"JSON decoding failed: {e}")
            return

        for post in data:
            item = APIScraperItem()
            item['userId'] = post.get('userId')
            item['id'] = post.get('id')
            item['title'] = post.get('title')
            item['body'] = post.get('body')
            yield item
