import hashlib, uuid
from app.models import CardDenomination
import redis
from app import redis1


class Utils():
    @staticmethod
    def validateParameter(param):
        if param :
            return param
        else :
            return None

    @staticmethod
    def isInteger(param):
        if None != param and param.isdigit():
            return True
        else :
            return False

    @staticmethod
    def getDenominationId(param):
        denomination = CardDenomination.query.filter_by(code=param).first()
        return denomination.id

    @staticmethod
    def validate_hash(hash, denomination_code, count, secret):
        m = hashlib.md5()
        m.update(denomination_code.encode())
        m.update(count.encode())
        m.update(secret.encode())
        temphash = m.hexdigest()
        print(temphash)
        return hash == temphash

    @staticmethod
    def hdm5_hash(denomination_code, count, secret):
        m = hashlib.md5()
        m.update(denomination_code.encode())
        m.update(count.encode())
        m.update(secret.encode())
        return m.digest()

    @staticmethod
    def generate_uuid():
        return str(uuid.uuid4())

    @staticmethod
    def redis_add():
        redisinstance = redis.StrictRedis()
        redisinstance.set('foo', 'bar')
        print(str(redisinstance.get('foo')))