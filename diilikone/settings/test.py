import os

DEBUG = True

SECRET_KEY = 'test_key'

SERVER_NAME = 'localhost:5000'

SQLALCHEMY_DATABASE_URI = os.environ.get(
  'TEST_DATABASE_URL',
  'postgres://localhost/diilikone_test'
)

TESTING = True
