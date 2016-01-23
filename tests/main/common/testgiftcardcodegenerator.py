import unittest, random
from app.main.common.GiftCardCodeHelper import GiftCardCodeHelper
from app.main.common.RedisHelper import RedisHelper


class GiftCardCodeGeneratorHelperTestCase(unittest.TestCase):
    def test_generate_pin(self):
        giftCardCodeGenerator = GiftCardCodeHelper()
        for i in range(10000):
            print(giftCardCodeGenerator.generate_pin())

            # print(giftCardCodeGenerator.generate_pin())
            # print(giftCardCodeGenerator.generate_pin())
            # print(giftCardCodeGenerator.generate_pin())
            # print(giftCardCodeGenerator.generate_pin())
            # print(giftCardCodeGenerator.generate_pin())
            # print(giftCardCodeGenerator.generate_pin())
            # print(giftCardCodeGenerator.generate_pin())

    def test_generate_serial(self):
        giftCardCodeHelper = GiftCardCodeHelper()
        a = 1
        print(giftCardCodeHelper.generate_serial(100, a, 'UPGC1S'))
        a += 100
        print(giftCardCodeHelper.generate_serial(100, a, 'UPGC1S'))
