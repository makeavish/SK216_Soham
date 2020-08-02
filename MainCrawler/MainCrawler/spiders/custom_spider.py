from bs4 import BeautifulSoup
import scrapy

class CustomSpider(scrapy.Spider):
    name = "custom_spider"
    start_urls = ['https://en.wikipedia.org/wiki/Scrapy']

    def parse(self, response):
        soup = BeautifulSoup(response.text, 'lxml')
        yield {
            'url':response.url,
            'title':soup.h1.string,
        }

        next_page = response.css('li.next a::attr(href)').get()
        if next_page is not None:
            yield response.follow(next_page, self.parse)
        