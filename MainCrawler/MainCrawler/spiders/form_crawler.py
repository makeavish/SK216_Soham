from bs4 import BeautifulSoup
import scrapy
import requests
from nltk.tokenize import RegexpTokenizer
from collections import OrderedDict
# from similarity import sim
import math 
import re

class FormCrawler(scrapy.Spider):
    name = "form_crawler"
    start_urls = []
    allowed_domains = []
    

    def __init__(self, *args, **kwargs): 
      super(FormCrawler, self).__init__(*args, **kwargs) 
      self.start_urls = [kwargs.get('start_url')] 
      self.allowed_domains = [kwargs.get('allowed_domain')]


    def parse(self, response):
        
        soup = BeautifulSoup(response.text, 'lxml')
        tokenizer = RegexpTokenizer(r'\w+')
        for script in soup(["script", "style"]):
            script.decompose()    # rip it out
        s = soup.get_text().strip()
        # print(s)
        # .encode('utf-8')
        #s='hello there there this is this hello'
        # s1=set()

        s2 = tokenizer.tokenize(s)
        s2.sort()
        
        
        yield {
            'url':response.url,
            'title':soup.h1.string,
            'text':s2,
        }

        for links in soup.find_all('a'):
            link = links.get('href')
            if link is not None:
                yield response.follow(link, self.parse)

#scrapy crawl form_crawler -a start_url='https://en.wikipedia.org/wiki/Cricket' -a allowed_domain='en.wikipedia.org' -o test.json