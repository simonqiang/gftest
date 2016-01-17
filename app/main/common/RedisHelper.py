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


    def redis_sadd(self, name_list, list):
        r = redis.StrictRedis(host=app.config['REDIS_HOST'], port=app.config['REDIS_PORT'])
        r.sadd(name_list, *list)

    def redis_srandmember(self, name_list, count):
        r = redis.StrictRedis(host=app.config['REDIS_HOST'], port=app.config['REDIS_PORT'])
        return r.srandmember(name_list, count)

    def redis_spop(self, name_list, count):
        # r = redis.StrictRedis(host=app.config['REDIS_HOST'], port=app.config['REDIS_PORT'])
        # return r.spop(name_list)
        pool = redis.ConnectionPool(host=app.config['REDIS_HOST'], port=app.config['REDIS_PORT'])
        r = redis.Redis(connection_pool=pool)
        pipe = r.pipeline()
        for index in range(count):
            pipe.spop(name_list)
        return pipe.execute()
