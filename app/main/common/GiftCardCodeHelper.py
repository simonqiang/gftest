import random, datetime
from .RedisHelper import RedisHelper
from app.models import CardDenomination, CardGiftCard
from app import db
from .utils import Utils


class GiftCardCodeHelper():
    giftcard_prefix = 'giftcard_prefix-'
    giftcard_serial_index = '-giftcard_serial_index'
    giftcard_list = '-giftcard_serial_list'
    giftcard_sets = '-giftcard_serial_sets'
    giftcard_flag = '-giftcard_serial_flag'

    # function to generates the serial
    # return a list of the serial
    def generate_serial(self, start, count, serialCode):
        serial_list = []
        for i in range(count):
            serial_list.append(serialCode + str(start + i).zfill(8))

        return serial_list

    def generate_pin(self):
        pinList = ['1', '2', '3', '4', '5', '6', '7', '8', '1', '2', '3', '4', '5', '6', '7', '8']
        random.shuffle(pinList)
        return ''.join(pinList)

    def insert_new_serial_into_redis(self, start, count, serialCode):
        redisHelper = RedisHelper()

        # increaee index
        redisHelper.redis_inc(count, self.giftcard_prefix + serialCode + self.giftcard_serial_index)

        # generates the list of the serial
        serial_list = self.generate_serial(start, count, serialCode)

        # insert into redis
        redisHelper.redis_sadd(self.giftcard_prefix + serialCode + self.giftcard_list, serial_list)

    def get_denomination_id(self, serialCode):
        denomination = CardDenomination.query.filter_by(serialCode=serialCode).all()
        if denomination and len(denomination) >= 1:
            return denomination[0].id

    def get_denomination_skuCode(self, serialCode):
        denomination = CardDenomination.query.filter_by(serialCode=serialCode).all()
        if denomination and len(denomination) >= 1:
            return denomination[0].skuCode

    def retrive_and_insert_to_db(self, serial_count, sku_start, serialCode, reference):
        reddisHelper = RedisHelper()

        # get serial list
        serial_list = reddisHelper.redis_spop_str(self.giftcard_prefix + serialCode + self.giftcard_list, serial_count)

        denomination_id = self.get_denomination_id(serialCode)

        sku_prefix = Utils.generate_skuCode_prefix(self.get_denomination_id(serialCode))

        current_time = datetime.datetime.utcnow()
        sku_count = 0
        for i in range(len(serial_list)):
            giftcard = CardGiftCard()
            giftcard.gfSerial = serial_list[i]
            giftcard.gfPin = Utils.generate_pin()
            giftcard.gfConsumed_dt = current_time
            giftcard.gfCreate_dt = current_time
            giftcard.gfReference = reference
            giftcard.gfStatus = 'X'
            giftcard.gfSKU = sku_prefix + str(sku_start + sku_count)
            giftcard.gfDenom_id = denomination_id
            sku_count += 1
            db.session.add(giftcard)

        db.session.commit()
