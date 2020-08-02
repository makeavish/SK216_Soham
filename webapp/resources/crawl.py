from flask import Response, request
from database.models import Crawl
from flask_restful import Resource

class CrawlsApi(Resource):
    def get(self):
        crawls = Crawl.objects().to_json()
        return Response(crawls, mimetype="application/json", status=200)

    def post(self):
        body = request.get_json()
        crawl =  Crawl(**body).save()
        id = crawl.id
        return {'id': str(id)}, 200
        
class CrawlApi(Resource):
    def put(self, id):
        body = request.get_json()
        Crawl.objects.get(id=id).update(**body)
        return '', 200
    
    def delete(self, id):
        crawl = Crawl.objects.get(id=id).delete()
        return '', 200

    def get(self, id):
        crawls = Crawl.objects.get(id=id).to_json()
        return Response(crawls, mimetype="application/json", status=200)