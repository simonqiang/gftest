from flask_restful import Resource, request
from ..common.utils import Utils
from ..common.GiftCardCodeHelper import GiftCardCodeHelper
from app import db
from manage import app
import sys, traceback
from config import Config

class GiftCard(Resource):
    def post(self):
        try:
            json_data = request.get_json(force=True)
            denomination_code = Utils.validateParameter(json_data['denomination_code'])
            count = Utils.validateParameter(json_data['count'])
            hash = Utils.validateParameter(json_data['hash'])
            sku = Utils.validateParameter(json_data['sku'])
            reference_value = Utils.validateParameter(json_data['reference'])

            # validate count
            if not Utils.isInteger(count):
                return 'invalid count', 200

            # validate hash
            if not Utils.validate_hash(hash, denomination_code, count, Config.GIFTCARD_SECRET_KEY):
                return 'invalid hash code', 200

            giftCardCodeHelper = GiftCardCodeHelper()
            # query denomination id
            serialCode = giftCardCodeHelper.get_denomination_serialCode(denomination_code)
            skuCode = giftCardCodeHelper.get_denomination_skuCode(denomination_code)

            # validate denomination id
            if not serialCode or not skuCode:
                return 'invalid denomination code', 200

            if not reference_value:
                return 'invlidate reference'

            if not Utils.isInteger(sku):
                return 'invalide sku', 200

            count = int(count)
            sku = int(sku)

            app.logger.info('serial_code : ' + serialCode + ' reference : ' + reference_value)
            giftCardCodeHelper.retrive_and_insert_to_db(count, sku, serialCode, skuCode, reference_value)
        except:
            app.logger.error('serial_code : ' + serialCode + ' reference : ' + reference_value)
            db.session.close()
            traceback.print_exc()
            return {'error ': str(sys.exc_info()[0])}

        return {'reference': reference_value, 'status': 200}
