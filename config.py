import os
basedir = os.path.abspath(os.path.dirname(__file__))
class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'you-will-never-guess'
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
        'sqlite:///' + os.path.join(basedir, 'app.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SHOP_ID = 5
    SECRET_KEY = 'SecretKey01'
    PAYWAY = 'advcash_rub'
    CURRENCYS = {
        'USD': 840,
        'EUR': 978,
        'RUB': 643,
    }
    URL_EUR = "https://pay.piastrix.com/ru/pay"
    URL_USD = "https://core.piastrix.com/bill/create"
    URL_RUB = "https://core.piastrix.com/invoice/create"
    EUR_REQUIRED = ['amount', 'currency', 'shop_id', 'shop_order_id']
    USD_REQUIRED = ['shop_amount', 'shop_currency', 'shop_id', 'shop_order_id',
                  'payer_currency']
    RUB_REQUIRED = ['amount', 'currency', 'payway', 'shop_id', 'shop_order_id']
