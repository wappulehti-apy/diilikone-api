import os

SECRET_KEY = 'development_key'

DEBUG = True

SQLALCHEMY_DATABASE_URI = os.environ.get(
    'DATABASE_URL',
    'postgres://localhost/diilikone'
)
CORS_HEADERS = 'Content-Type'

MAIL_SUPPRESS_SEND = True

MAIL_SERVER = os.environ.get('MAIL_SERVER')

MAIL_PORT = int(os.environ.get('MAIL_PORT'))

MAIL_USERNAME = os.environ.get('MAIL_USER')

MAIL_PASSWORD = os.environ.get('MAIL_KEY')

MAIL_DEFAULT_SENDER = os.environ.get('MAIL_SENDER')
MAIL_USE_TLS = bool(os.environ.get('MAIL_USE_TLS'))
