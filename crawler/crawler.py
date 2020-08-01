import requests
import re
from bs4 import BeautifulSoup
from queue import PriorityQueue
from similarity import sim
import os


def crawlL(seed_url):
    visited = set()
    queue = PriorityQueue()
    queue.put((1, seed_url))

    while queue.qsize() != 0:
        link = queue.get()

        try:
            headers = {
                "User-Agent": "Mozilla/5.0 (Windows NT 6.3; WOW64; rv:38.0) Gecko/20100101 Firefox/38.0"}
            # link[1] = requests.get(link[1]).url
            page = requests.get(link[1])
            page_content = BeautifulSoup(page.content, 'html.parser')
            # print("Test1")
        except:
            try:
                link[1] = "https://" + link[1]
                link[1] = requests.get(link[1]).url
                page = requests.get(link[1])
                page_content = BeautifulSoup(page.content, 'html.parser')
            except:
                print("Invalid Link")
                continue
        for links in page_content.find_all('a'):
            # print("Test2")
            links = links.get('href')
            if links not in visited:
                try:
                    score = sim(seed_url, links)
                    visited.add(links)
                    queue.put((-score, str(links)))
                except Exception as E:
                    # print(E)
                    continue

        

