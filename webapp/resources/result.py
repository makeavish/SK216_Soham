from flask import Response, request
from database.models import Results
from flask_restful import Resource
from flask_jwt_extended import jwt_required

class ResultsApi(Resource):
    @jwt_required
    def get(self):
        results = Results.objects().to_json()
        return Response(results, mimetype="application/json", status=200)

    @jwt_required
    def post(self):
        body = request.get_json()
        results =  Results(**body).save()
        id = results.id
        return {'id': str(id)}, 200

class ResultsApiID(Resource):
    @jwt_required
    def put(self, id):
        body = request.get_json()
        Results.objects.get(id=id).update(**body)
        return '', 200

    def get(self, id):
        results = Results.objects.get(id=id).to_json()
        return Response(results, mimetype="application/json", status=200)
        