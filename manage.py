#!/usr/bin/env python
import os, logging
from app import create_app, db
from app.models import User, Role, CardDenomination, CardGiftCard
from flask.ext.script import Manager, Shell
from flask.ext.migrate import Migrate, MigrateCommand
from logging.handlers import RotatingFileHandler

app = create_app(os.getenv('FLASK_CONFIG') or 'default')
manager = Manager(app)
migrate = Migrate(app, db)

handler = RotatingFileHandler('giftcard.log', maxBytes=20000, backupCount=6)
handler.setLevel(logging.INFO)
app.logger.addHandler(handler)

def make_shell_context():
    return dict(app=app, db=db, User=User, Role=Role, CardDenomination=CardDenomination, CardGiftCard=CardGiftCard)
manager.add_command("shell", Shell(make_context=make_shell_context))
manager.add_command('db', MigrateCommand)


@manager.command
def test():
    """Run the unit tests."""
    import unittest
    tests = unittest.TestLoader().discover('tests')
    unittest.TextTestRunner(verbosity=2).run(tests)


if __name__ == '__main__':
    manager.run()
