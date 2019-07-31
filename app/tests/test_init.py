import sys
sys.path.append("flask-comics-api")
from app import app



def test_all_comics(): 
  print(app)
  assert False