from flask_restful import Resource, request
from ..common.utils import Utils

TODOS = {
    'todo1': {'task': 'build an API'},
    'todo2': {'task': '?????'},
    'todo3': {'task': 'profit!'},
}

result = {
    'reference': ''
}


class GiftCard(Resource):
    def post(self):
        json_data = request.get_json(force=True)
        denomination_code = Utils.validateParameter(json_data['denomination_code'])
        count = Utils.validateParameter(json_data['count'])
        hash = Utils.validateParameter(json_data['hash'])

        # validate count
        if not Utils.isInteger(count):
            return 'invalid count', 200
        # validate hash
        if not Utils.validate_hash(hash, denomination_code, count, ''):
            return 'invalid hash code', 200
        # query denomination id
        denomination_id = Utils.getDenominationId(denomination_code)

        # validate denomination id
        if not denomination_id:
            return 'invalid denomination code', 200

        reference_value = Utils.generate_uuid()

        return {'reference': reference_value}
