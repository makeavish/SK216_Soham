from .crawl import CrawlsApi, CrawlApi

def initialize_routes(api):
    api.add_resource(CrawlsApi, '/api/crawls')
    api.add_resource(CrawlApi, '/api/crawls/<id>')