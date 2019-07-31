import json

def test_get_empty(client): 
  res = client.get('/comics')
  assert res.status_code == 200
  assert json.loads(res.data.decode()) == []

def test_comic(sample_comic): 
  assert sample_comic.id == 1
  assert sample_comic.title == 'Shade The Changing Girl'
  assert sample_comic.issues == 12

def test_character(sample_character): 
  assert sample_character.id == 1 
  assert sample_character.name == 'Loma Shade'
