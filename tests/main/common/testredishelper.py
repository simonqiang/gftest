import unittest
from app.main.common.RedisHelper import RedisHelper
from app.main.jobs.giftCardSchedule import GiftCardSchedule

class RedisHelperTestCase(unittest.TestCase):
    def test_redis_srandmember(self):
        redishelper = RedisHelper()
        aList = redishelper.redis_srandmember('liuqiang-sets', 4)
        print(aList)

    def test_redis_sadd_spop(self):
        redishelper = RedisHelper()
        mylist = []
        mylist.append("1")
        mylist.append("2")
        mylist.append("3")
        mylist.append("4")
        mylist.append("5")
        mylist.append("6")
        mylist.append("7")
        mylist.append("8")
        redishelper = RedisHelper()
        redishelper.redis_sadd('liuqiang-sets', mylist)

        self.assertEqual(8, redishelper.redis_scard('liuqiang-sets'))
        print(redishelper.redis_scard('liuqiang-sets'))

        aList = redishelper.redis_spop_str('liuqiang-sets', 4)
        print(aList)
        self.assertEqual(4, len(aList))
        aList = redishelper.redis_spop_str('liuqiang-sets', 4)
        print(aList)
        self.assertEqual(4, len(aList))

    def test_redis_incr_get(self):
        redisHelper = RedisHelper()
        redisHelper.redis_set('index1', 0)
        self.assertEqual(10, redisHelper.redis_inc('index1', 10))
        self.assertEqual(10, int(redisHelper.redis_get('index1')))

    def test_get_flag(self):
        redisHelper = RedisHelper()
        if redisHelper.redis_get('liuqiang_flag'):
            print("there is something")
        else:
            print("there is None")

    def test_set_flag(self):
        redisHelper = RedisHelper()
        redisHelper.redis_set_expire('liuqiang_flag', 1, 5)

    def test_schedule(self):
        giftCardSchedule = GiftCardSchedule()
        giftCardSchedule.test()

if __name__ == '__main__':
    unittest.main()
