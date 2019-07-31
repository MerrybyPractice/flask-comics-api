import os
print('pwd---', os.getcwd())

# import sys
# sys.path.append("..")
from app import create_app, db
from config import Config
from models import Comic, Character

import pytest

class TestConfig(Config): 
  SQLALCHEMY_DATABASE_URI = "sqlite://"

@pytest.fixture(scope='session')
def client(): 
  app = create_app(TestConfig)
  app_context = app.app_context()
  app_context.push()
  db.create_all()
  with app.test_client() as client: 
    yield client
  db.session.remove()
  db.drop_all()
  app_context.pop()
 

  @pytest.fixture
  def sample_comic(client): 
    comic = Comic(title='Shade The Changing Girl', issues='12')
    db.session.add(comic) 
    db.session.commit() 
    return comic

  @pytest.fixture
  def sample_comic(sample_comic): 
    character = Character(name='Loma Shade')
    db.session.add(character)
    db.session.commit()
    return character
