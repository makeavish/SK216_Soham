from bs4 import BeautifulSoup
import scrapy
import requests
from nltk.tokenize import RegexpTokenizer
from collections import OrderedDict
import math 
import re

class TextCrawler(scrapy.Spider):
    name = "text_crawler"
    start_urls = []

    def __init__(self, *args, **kwargs): 
      super(TextCrawler, self).__init__(*args, **kwargs) 
      self.start_urls = [kwargs.get('start_url')] 

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

#scrapy crawl text_crawler -a start_url=<url> -o <file>.json