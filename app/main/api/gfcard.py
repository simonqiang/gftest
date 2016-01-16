from flask_restful import  Resource, request
from ..common.utils import Utils

TODOS = {
    'todo1': {'task': 'build an API'},
    'todo2': {'task': '?????'},
    'todo3': {'task': 'profit!'},
}

class GiftCard(Resource):
    def post(self):
        json_data = request.get_json(force=True)
        denomination_code = Utils.validateParameter(json_data['denomination_code'])
        count = Utils.validateParameter(json_data['count'])
        hash = Utils.validateParameter(json_data['hash'])

        if not Utils.isInteger(count):
            return 'invalid count'

        if not Utils.validate_hash(hash, denomination_code, count, ''):
            return 'invalid hash code', 200

        return TODOS