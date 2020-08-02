from flask import Response, request
from database.models import Results
from flask_restful import Resource
from flask_jwt_extended import jwt_required

from mongoengine.errors import FieldDoesNotExist, \
NotUniqueError, DoesNotExist, ValidationError, InvalidQueryError
from resources.errors import SchemaValidationError, ResultAlreadyExistsError, \
InternalServerError, UpdatingResultError, DeletingResultError, ResultNotExistsError

class ResultsApi(Resource):
    # @jwt_required
    # def get(self):
    #     results = Results.objects().to_json()
    #     return Response(results, mimetype="application/json", status=200)

    @jwt_required
    def post(self):
        try:
            body = request.get_json()
            results =  Results(**body).save()
            id = results.id
            return {'id': str(id)}, 200
        except (FieldDoesNotExist, ValidationError):
            raise SchemaValidationError
        except NotUniqueError:
            raise ResultAlreadyExistsError
        except Exception as e:
            raise InternalServerError

class ResultsApiID(Resource):
    @jwt_required
    def put(self, id):
        try:
            body = request.get_json()
            Results.objects.get(id=id).update(**body)
            return '', 200
        except InvalidQueryError:
            raise SchemaValidationError
        except DoesNotExist:
            raise UpdatingResultError
        except Exception:
            raise InternalServerError 

    def get(self, id):
        try:
            results = Results.objects.get(id=id).to_json()
            return Response(results, mimetype="application/json", status=200)
        except DoesNotExist:
            raise ResultNotExistsError
        except Exception:
            raise InternalServerError
        