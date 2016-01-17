from flask import Flask
from flask.ext.bootstrap import Bootstrap
from flask.ext.mail import Mail
from flask.ext.moment import Moment
from flask.ext.sqlalchemy import SQLAlchemy
from config import config
from flask.ext.redis import Redis

bootstrap = Bootstrap()
mail = Mail()
moment = Moment()
db = SQLAlchemy()
redis1 = Redis()

def create_app(config_name):
    app = Flask(__name__)
    app.config.from_object(config[config_name])
    config[config_name].init_app(app)
    app.config['REDIS_HOST'] = 'localhost'
    app.config['REDIS_PORT'] = 6379
    app.config['REDIS_DB'] = 0

    bootstrap.init_app(app)
    mail.init_app(app)
    moment.init_app(app)
    db.init_app(app)

    redis1.init_app(app)


    from .main import main as main_blueprint
    # from .main.common import common
    app.register_blueprint(main_blueprint)
    # app.register_blueprint(common)

    return app

