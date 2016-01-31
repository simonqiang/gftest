import os, logging
from app import create_app
from logging.handlers import RotatingFileHandler

app = create_app(os.getenv('FLASK_CONFIG') or 'default')

handler = RotatingFileHandler('giftcard.log', maxBytes=20000, backupCount=6)
handler.setLevel(logging.INFO)
app.logger.addHandler(handler)

if __name__ == '__main__':
    app.run()
