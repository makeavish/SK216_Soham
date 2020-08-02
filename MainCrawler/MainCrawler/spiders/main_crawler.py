from bs4 import BeautifulSoup
import scrapy
import requests
from nltk.tokenize import RegexpTokenizer
from collections import OrderedDict
# from similarity import sim
import math 
import re

class MainCrawler(scrapy.Spider):
    name = "main_crawler"
    start_urls = ["https://en.wikipedia.org/wiki/Scrapy"]
    

    # def __init__(self, *args, **kwargs): 
    #   super(MainCrawler, self).__init__(*args, **kwargs) 
    #   self.start_urls = [kwargs.get('start_url')] 

    page = requests.get(start_urls[0])
    soup = BeautifulSoup(page.text, 'lxml')

    def soupToText(self, soup):
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
        return s2

    def sumofFreq(self, d1, d2):
        sum = 0
        for word in d1:
            if word in d2:
                sum = sum+(d1[word]*d2[word])
        return sum

    def mag(self, dic1):
        mag = 0
        for word, value in dic1.items():
            mag = mag+(value*value)
        return mag

    def dict(self, text):
        dict = {}
        for word in text:
            if word in dict:
                dict[word] += 1
            else:
                dict[word] = 1
        # for word, freq in dict.items():
            # print(word+":"+str(freq))
        return dict

    def sim(self, link1, link2):
        doc1 = soupToText(link1)
        doc2 = soupToText(link2)
        dic1 = dict(doc1)
        dic2 = dict(doc2)
        fsum = sumofFreq(dic1, dic2)
        mag1 = mag(dic1)
        mag2 = mag(dic2)
        if mag1==0 or mag2==0:
            return 0
        cos = float(fsum/(math.sqrt(mag1)*math.sqrt(mag2)))
        return float(cos)

    def parse(self, response):
        soup1 = BeautifulSoup(response.text, 'lxml')
        # score = sim(soup, soup1)
        
        yield {
            'url':response.url,
            'title':soup1.h1.string,
        }

        for links in soup1.find_all('a'):
            link = links.get('href')
            if link is not None:
                yield response.follow(link, self.parse,priority=1)
        