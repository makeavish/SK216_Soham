# from google.py import find
import sys
import os
try: 
    from googlesearch import search 
except ImportError:  
    print("No module named 'google' found") 
  
# to search 
# query = "Geeksforgeeks"
  
def find(query,n):
    ans=[]
    for j in search(query, tld="com", num=n,stop=n, pause=2): 
        ans.append(j)
    return ans

def start_crawl(urls):
    command = "scrapy crawl main_crawler -a start-url="
    for url in urls:
        command+="\'"+url+"\',"
    os.system(command)


query=sys.argv[1]
urls = find(query, 1)
start_crawl(urls)
