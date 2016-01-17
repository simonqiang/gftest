import unittest
from app.main.common.utils import Utils
from app import create_app, db

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

if __name__ == '__main__':
    unittest.main()