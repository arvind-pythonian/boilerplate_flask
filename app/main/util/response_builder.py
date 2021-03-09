import gzip
import json
from datetime import datetime
from bson import ObjectId
from flask import make_response


class ResponseService:
    @staticmethod
    def build(data, statusCode, status, message):
        response = dict()
        data = JSONEncoder().encode(data)
        response['status'] = status
        response['message'] = message
        response['statusCode'] = statusCode
        response['data'] = json.loads(data)
        return ResponseService.encodeResponse(response)

    @staticmethod
    def buildPagination(data, metaData, statusCode, status, message):
        response = dict()
        data = JSONEncoder().encode(data)
        response['status'] = status
        response['message'] = message
        response['statusCode'] = statusCode
        response['metaData'] = metaData
        response['data'] = json.loads(data)
        return ResponseService.encodeResponse(response)

    @staticmethod
    def encodeResponse(response):
        content = gzip.compress(json.dumps(response).encode('utf8'), 5)
        response = make_response(
            content)
        response.headers["Content-Type"] = "application/json"
        response.headers['Content-Encoding'] = 'gzip'
        return response


class JSONEncoder(json.JSONEncoder):
    def default(self, o):
        if isinstance(o, (ObjectId, datetime)):
            return str(o)
        return json.JSONEncoder.default(self, o)


JSONEncode = JSONEncoder(indent=2)
