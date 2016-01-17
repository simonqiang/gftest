from flask import Blueprint

main = Blueprint('main', __name__)

from . import views, errors

from flask_restful import Api
from .api.gfcard import GiftCard

api = Api(main)

api.add_resource(GiftCard, '/giftcard/request')
