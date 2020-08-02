from .crawl import CrawlsApi, CrawlsApiID
from .auth import SignupApi, LoginApi
from .result import ResultsApi, ResultsApiID

def initialize_routes(api):
    api.add_resource(CrawlsApi, '/api/crawls')
    api.add_resource(CrawlsApiID, '/api/crawls/<id>')
    api.add_resource(ResultsApi, '/api/results')
    api.add_resource(ResultsApiID, '/api/results/<id>')
    api.add_resource(SignupApi, '/api/auth/signup')
    api.add_resource(LoginApi, '/api/auth/login')
