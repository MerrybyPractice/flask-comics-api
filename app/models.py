from app import db

class Comic(db.Model): 
  id = db.Column(db.Integer, primary_key=True) 
  title = db.Column(db.String(256), unique=False) 
  issues = db.Column(db.Integer, unique=False, nullable=True)
  characters = db.relationship("Character", backref="comic", lazy=True)

  def to_dict(self): 
    return{'id': self.id, 'title': self.title, 'issues': self.issues} 
  
class Character(db.Model): 
  id = db.Column(db.Integer, primary_key=True)
  name = db.Column(db.String(256), unique=True)
  comic_id = db.Column(db.Integer, db.ForeignKey('band.id'), nullable=True) 

  def to_dict(self): 
    return{'id': self.id, 'name': self.name}
