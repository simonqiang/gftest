import unittest, datetime
from app.main.common.utils import Utils
from app import create_app, db
from app.models import CardGiftCard, CardDenomination

class UtilsTestCase(unittest.TestCase):
    def setUp(self):
        self.app = create_app('development')
        self.app_context = self.app.app_context()
        self.app_context.push()

    def tearDown(self):
        db.session.remove()
        self.app_context.pop()

    def test_validateParameter(self):
        self.assertIsNone(Utils.validateParameter(""))
        self.assertIsNone(Utils.validateParameter(None))
        print(Utils.validateParameter('money') + 'dfdfdfdf')
        self.assertEqual('money', Utils.validateParameter('money'))

    def test_isInteger(self):
        self.assertTrue(Utils.isInteger('1254'))
        self.assertFalse(Utils.isInteger('1254.343'))
        self.assertFalse(Utils.isInteger('1254dfdf'))
        self.assertFalse(Utils.isInteger(None))

    def test_validate_hash(self):
        self.assertTrue(Utils.validate_hash('f40b6cfbb93ce812fa9f92c2827543b7', "c74501e2-3910-4d8e-9192-98f67bdefe69", "A1dy1gV6Ri12H13B", ""))

    def test_getDenomiation(self):
        self.assertEquals(1, Utils.getDenominationId('10'))

    def test_generate_uuid(self):
        tempuuid = Utils.generate_uuid()
        print(tempuuid)
        self.assertIsNotNone(tempuuid)

    def test_redis_add(self):
        Utils.redis_add()

    def test_mode_giftcard(self):
        giftcard = CardGiftCard()
        giftcard.gfSerial = 'serial1'
        giftcard.gfPin = 'pin1'
        giftcard.gfConsumed_dt = datetime.datetime.now()
        giftcard.gfConsumed_dt = datetime.datetime.now()
        giftcard.gfReference = 'reference1'
        giftcard.gfStatus = 'X'
        giftcard.gfSKU = 'SKU1'
        giftcard.gfDenom_id = 1

        giftcard2 = CardGiftCard()
        giftcard2.gfSerial = 'serial2'
        giftcard2.gfPin = 'pin2'
        giftcard2.gfConsumed_dt = datetime.datetime.now()
        giftcard2.gfConsumed_dt = datetime.datetime.now()
        giftcard2.gfReference = 'reference2'
        giftcard2.gfStatus = 'X'
        giftcard2.gfSKU = 'SKU2'
        giftcard2.gfDenom_id = 1
        db.session().add(giftcard)
        db.session().add(giftcard2)
        db.session().commit()

    def test_mode_giftcard_select(self):
        sku_list = CardGiftCard.query.filter_by(gfDenom_id=1).all()
        print(sku_list[0].gfSerial)

    def test_mode_cardDenimination(self):
        cardDenom = CardDenomination.query.filter_by(serialCode='UPGC1S').all()
        print(cardDenom[0].id)

    def test_generate_sku_prefix(self):
        print(Utils.generate_skuCode_prefix('UP010'))


if __name__ == '__main__':
    unittest.main()