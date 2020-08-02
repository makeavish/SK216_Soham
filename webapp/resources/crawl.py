from flask import Response, request
from database.models import Crawl
from flask_restful import Resource
from flask_jwt_extended import jwt_required

from mongoengine.errors import FieldDoesNotExist, \
NotUniqueError, DoesNotExist, ValidationError, InvalidQueryError
from resources.errors import SchemaValidationError, CrawlAlreadyExistsError, \
InternalServerError, UpdatingCrawlError, DeletingCrawlError, CrawlNotExistsError


class CrawlsApi(Resource):
    # @jwt_required
    # def get(self):
    #     crawls = Crawl.objects().to_json()
    #     return Response(crawls, mimetype="application/json", status=200)

    @jwt_required
    def post(self):
        try:
            body = request.get_json()
            crawl =  Crawl(**body).save()
            id = crawl.id
            return {'id': str(id)}, 200
        except (FieldDoesNotExist, ValidationError):
            raise SchemaValidationError
        except NotUniqueError:
            raise CrawlAlreadyExistsError
        except Exception as e:
            raise InternalServerError
        
class CrawlsApiID(Resource):

    @jwt_required
    def put(self, id):
        try:
            body = request.get_json()
            Crawl.objects.get(id=id).update(**body)
            return '', 200
        except InvalidQueryError:
            raise SchemaValidationError
        except DoesNotExist:
            raise UpdatingCrawlError
        except Exception:
            raise InternalServerError 

    @jwt_required
    def delete(self, id):
        try:
            crawl = Crawl.objects.get(id=id).delete()
            return '', 200
        except DoesNotExist:
            raise DeletingCrawlError
        except Exception:
            raise InternalServerError

    def get(self, id):
        try:
            crawls = Crawl.objects.get(id=id).to_json()
            return Response(crawls, mimetype="application/json", status=200)
        except DoesNotExist:
            raise CrawlNotExistsError
        except Exception:
            raise InternalServerError
