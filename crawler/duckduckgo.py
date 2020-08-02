from duckduckpy import query
response = query('Python')
for i in response.related_topics:
    print(i.first_url)
