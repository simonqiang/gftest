from config import Config
from app.main.common.GiftCardCodeHelper import GiftCardCodeHelper
from ..common.RedisHelper import RedisHelper
import sys, traceback


class GiftCardSchedule(object):
    def test(self):
        print("running jobs")
        giftCardCodeHelper = GiftCardCodeHelper()
        redisHelper = RedisHelper()
        if not redisHelper.redis_get(giftCardCodeHelper.giftcard_prefix + giftCardCodeHelper.giftcard_flag):

            redisHelper.redis_set_expire(giftCardCodeHelper.giftcard_prefix + giftCardCodeHelper.giftcard_flag, '1',
                                         400)

            for serial_code in Config.SERIAL_CODES:
                try:
                    # check if there is enough serial
                    current_count = redisHelper.redis_scard(
                        giftCardCodeHelper.giftcard_prefix + serial_code + giftCardCodeHelper.giftcard_list)
                    if current_count <= giftCardCodeHelper.giftcard_min_count:
                        # if the index is None or index + generration cout is bigger than 99999999 set index to 1
                        index = int(redisHelper.redis_get(
                            giftCardCodeHelper.giftcard_prefix + serial_code + giftCardCodeHelper.giftcard_serial_index))
                        if not index or (
                                index + giftCardCodeHelper.giftcard_generation_count > giftCardCodeHelper.giftcard_generation_max):
                            index = 1;

                        redisHelper.redis_inc(
                            giftCardCodeHelper.giftcard_prefix + serial_code + giftCardCodeHelper.giftcard_serial_index,
                            giftCardCodeHelper.giftcard_generation_count)
                        # insert new serial in redis
                        print('insert new serial in reids')
                        serial_list = giftCardCodeHelper.generate_serial(index,
                                                                         giftCardCodeHelper.giftcard_generation_count,
                                                                         serial_code)
                        redisHelper.redis_sadd(
                            giftCardCodeHelper.giftcard_prefix + serial_code + giftCardCodeHelper.giftcard_list,
                            serial_list)
                except:
                    redisHelper.redis_delete(giftCardCodeHelper.giftcard_prefix + giftCardCodeHelper.giftcard_flag)
                    e = sys.exc_info()[0]
                    traceback.print_exc()
                    return {'error ': str(e)}

            redisHelper.redis_delete(giftCardCodeHelper.giftcard_prefix + giftCardCodeHelper.giftcard_flag)
