from .crawl import CrawlsApi, CrawlApi
from .auth import SignupApi

def initialize_routes(api):
    api.add_resource(CrawlsApi, '/api/crawls')
    api.add_resource(CrawlApi, '/api/crawls/<id>')
    api.add_resource(SignupApi, '/api/auth/signup')