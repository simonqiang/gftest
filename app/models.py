import datetime
from . import db
from sqlalchemy.dialects.mysql import BIGINT, INTEGER
from sqlalchemy import DateTime, func, text


class Role(db.Model):
    __tablename__ = 'roles'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), unique=True)
    users = db.relationship('User', backref='role', lazy='dynamic')

    def __repr__(self):
        return '<Role %r>' % self.name


class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(BIGINT(display_width=20, unsigned=True), primary_key=True)
    username = db.Column(db.String(64), unique=True, index=True)
    fristname = db.Column(db.String(64), unique=True, index=True)
    lastname = db.Column(db.String(64), unique=True, index=True)
    middlename = db.Column(db.String(64), unique=True, index=True)
    role_id = db.Column(db.Integer, db.ForeignKey('roles.id'))

    def __repr__(self):
        return '<User %r>' % self.username


class CardDenomination(db.Model):
    __tablename__ = 'card_denomination'
    id = db.Column(INTEGER(unsigned=True, display_width=11), primary_key=True, autoincrement=True, nullable=False)
    code = db.Column(db.String(8, collation='utf8_unicode_ci'), unique=True, index=True, nullable=False)
    point = db.Column(db.Integer, nullable=False)
    amount = db.Column(db.Integer, nullable=False)
    description = db.Column(db.String(255, collation='utf8_unicode_ci'), nullable=True, default=None)
    serialCode = db.Column(db.String(8, collation='utf8_unicode_ci'), unique=True, index=True, nullable=False)
    skuCode = db.Column(db.String(8, collation='utf8_unicode_ci'), unique=True, index=True, nullable=False)

    def __repr__(self):
        return '<card_denomination_code %r>' % self.code


class CardGiftCard(db.Model):
    __tablename__ = 'card_giftcard'
    id = db.Column(BIGINT(unsigned=True, display_width=20), primary_key=True, autoincrement=True, nullable=False)
    gfSerial = db.Column(db.String(20, collation='utf8_unicode_ci'), unique=True, index=True, nullable=False)
    gfPin = db.Column(db.String(20, collation='utf8_unicode_ci'), unique=True, index=True, nullable=False)
    gfCreate_dt = db.Column(db.DateTime, default=datetime.datetime.utcnow(), nullable=False)
    gfConsumed_dt = db.Column(DateTime, default=func.now(), nullable=False)
    gfReference = db.Column(db.String(64, collation='utf8_unicode_ci'), nullable=False, index=True)
    gfStatus = db.Column(db.String(1, collation='utf8_unicode_ci'), nullable=False, index=True)
    gfSKU = db.Column(db.String(32, collation='utf8_unicode_ci'), nullable=False)
    gfOrderID = db.Column(db.String(64, collation='utf8_unicode_ci'), nullable=True, default=text("NULL"), index=True)
    gfDenom_id = db.Column(INTEGER(unsigned=True, display_width=11), db.ForeignKey('card_denomination.id'), index=True, nullable=False,)

    def __repr__(self):
        return '<card_gfcard_SKU %r>' % self.gfSKU
