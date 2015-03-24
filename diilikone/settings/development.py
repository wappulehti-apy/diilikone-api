import os

SECRET_KEY = 'development_key'

DEBUG = True

SQLALCHEMY_DATABASE_URI = os.environ.get(
    'DATABASE_URL',
    'postgres://localhost/diilikone'
)
CORS_HEADERS = 'Content-Type'
