import sys
sys.path.append("flask-comics-api")
from app import app

import pytest

class TestConfig(Config): 
  SQLALCHEMY_DATABASE_URI = "sqlite://"

@pytest.fixture(scope='session')
def client(): 
  return app.test(client) 
