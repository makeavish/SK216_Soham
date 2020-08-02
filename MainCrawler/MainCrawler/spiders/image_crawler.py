from bs4 import BeautifulSoup
import scrapy
import requests
from nltk.tokenize import RegexpTokenizer
from collections import OrderedDict
import math 
import re

class ImageCrawler(scrapy.Spider):
    name = "image_crawler"
    start_urls = []

    def __init__(self, *args, **kwargs): 
      super(ImageCrawler, self).__init__(*args, **kwargs) 
      self.start_urls = [kwargs.get('start_url')] 

    def parse(self, response):
        soup = BeautifulSoup(response.text, 'lxml')
        s2 = []

        for img in soup.find_all('img'):
            s2.append(img.get('src'))
        
        yield {
            'url':response.url,
            'title':soup.h1.string,
            'images':s2,
        }

#scrapy crawl img_crawler -a start_url=<url> -o <file>.json