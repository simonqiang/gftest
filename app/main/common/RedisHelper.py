import redis
from manage import app

class RedisHelper():
    def redis_lpush_list(self, name_list, list):
        pool = redis.ConnectionPool(host=app.config['REDIS_HOST'], port=app.config['REDIS_PORT'])
        r = redis.Redis(connection_pool=pool)
        pipe = r.pipeline()
        pipe.lpush(name_list, *list)
        pipe.execute()

    def redis_rpop(self, name_list):
        r = redis.StrictRedis(host=app.config['REDIS_HOST'], port=app.config['REDIS_PORT'])
        return str(r.rpop(name_list), encoding='UTF-8')

    def redis_sadd(self, name_sets, list):
        r = redis.StrictRedis(host=app.config['REDIS_HOST'], port=app.config['REDIS_PORT'])
        r.sadd(name_sets, *list)

    def redis_srandmember(self, name_sets, count):
        r = redis.StrictRedis(host=app.config['REDIS_HOST'], port=app.config['REDIS_PORT'])
        return r.srandmember(name_sets, count)

    def redis_spop_str(self, name_sets, count):
        mylist = self.redis_spop(name_sets, count)

        # convert byte to string
        for i in range(len(mylist)):
            mylist[i] = str(mylist[i], encoding='UTF-8')

        return mylist

    def redis_spop(self, name_sets, count):
        # r = redis.StrictRedis(host=app.config['REDIS_HOST'], port=app.config['REDIS_PORT'])
        # return r.spop(name_list)
        pool = redis.ConnectionPool(host=app.config['REDIS_HOST'], port=app.config['REDIS_PORT'])
        r = redis.Redis(connection_pool=pool)
        pipe = r.pipeline()
        for index in range(count):
            pipe.spop(name_sets)
        return pipe.execute()

    def redis_scard(self, name_sets):
        r = redis.StrictRedis(host=app.config['REDIS_HOST'], port=app.config['REDIS_PORT'])
        return int(r.scard(name_sets))

    def redis_delete(self, name_index):
        r = redis.StrictRedis(host=app.config['REDIS_HOST'], port=app.config['REDIS_PORT'])
        r.delete(name_index)

    def redis_set(self, name_index, value):
        r = redis.StrictRedis(host=app.config['REDIS_HOST'], port=app.config['REDIS_PORT'])
        r.set(name_index, value)

    def redis_get_str(self, name_index):
        r = redis.StrictRedis(host=app.config['REDIS_HOST'], port=app.config['REDIS_PORT'])
        return str(r.get(name_index), encoding='UTF-8')

    def redis_get(self, name_index):
        r = redis.StrictRedis(host=app.config['REDIS_HOST'], port=app.config['REDIS_PORT'])
        return r.get(name_index)

    def redis_set_expire(self, name_index, value, expire):
        r = redis.StrictRedis(host=app.config['REDIS_HOST'], port=app.config['REDIS_PORT'])
        r.set(name_index, value, expire)

    def redis_inc(self, name_index, amount):
        r = redis.StrictRedis(host=app.config['REDIS_HOST'], port=app.config['REDIS_PORT'])
        return r.incr(name_index, amount)
