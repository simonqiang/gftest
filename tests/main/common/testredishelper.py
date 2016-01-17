import unittest
from app.main.common.RedisHelper import RedisHelper

class RedisHelperTestCase(unittest.TestCase):
    def test_redis_lpush_list(self):
        mylist = []
        mylist.append("1")
        mylist.append("2")
        mylist.append("3")
        mylist.append("4")
        mylist.append("5")
        mylist.append("6")
        mylist.append("7")
        mylist.append("8")
        print(mylist)

        redishelper = RedisHelper()
        redishelper.redis_lpush_list('liuqiang-list', mylist)

    def test_redis_rpop_list(self):
        redishelper = RedisHelper()
        print(redishelper.redis_rpop('liuqiang-list'))

    def test_redis_sadd_list(self):
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

    def test_redis_srandmember(self):
        redishelper = RedisHelper()
        aList = redishelper.redis_srandmember('liuqiang-sets', 4)
        print(aList)

    def test_redis_spop(self):
        redishelper = RedisHelper()
        for index in range(10000) :
            aList = redishelper.redis_spop('liuqiang-sets', 4)
            print(aList)

if __name__ == '__main__':
    unittest.main()
