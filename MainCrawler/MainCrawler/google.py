# pip install google
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

# j=find("particle physics",10)
# print(j)