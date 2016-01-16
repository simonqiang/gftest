import hashlib, binascii
from app.models import CardDenomination


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

        return hash == temphash

    @staticmethod
    def hdm5_hash(denomination_code, count, secret):
        m = hashlib.md5()
        m.update(denomination_code.encode())
        m.update(count.encode())
        m.update(secret.encode())
        return m.digest()
