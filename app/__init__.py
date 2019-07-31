from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
db = SQLAlchemy() 
migrate = Migrate() 

def create_app(ConfigClass): 

  app = Flask(__name__)

  app.config.from_object(ConfigClass) 

  db.init_app(app) 

  migrate.init_app(app, db) 

  with app.app_context(): 

    @app.route('/comics', methods=['GET'])
    def all_comics(): 
      comics = [comic.to_dict for comic in Comic.query.all()] 
      return jsonify(comics)

    @app.route('/comics/<int:id>', methods=['GET'])
    def one_comic(id): 
      comic = Comic.query.get(id) 
      return jsonify(comic) 

    @app.route('/comics', methods=['POST'])  
    def create_comic(): 
      comic_info = request.json or request.form or request.values
      comic = Comic(title=comic_info.get('title'), issues=comic_info.get('issues')) 
      db.session.add(comic) 
      db.session.commit() 

      return jsonify(comic.to_dict()) 

    @app.route('/comics/<int:id>', methods=['DELETE'])
    def delete_comic(id):  
      pass 

    @app.route('/comics/<int:id>', methods=['PUT'])
    def  update_comic(id): 
      pass

    @app.route('/characters', methods=['GET'])  
    def all_artists():
      characters = [character.to_dict() for character in Character.query.all()]
      return jsonify(artists) 

    @app.route('/characters/<int:id>', methods=['GET'])
    def one_character(id): 
      character = Character.query.get(id) 
      return jsonify(character.to_dict()) 

    @app.route('/characters', methods=['POST'])  
    def create_character(): 
      character_info= request.json or request.form or request.values 
      character = Character(name=character_info.get('name'), comic_id=character_info.get('comic'))
      db.session.add(character) 
      db.session.commit() 

    @app.route('/characters/<int:id>', methods=['DELETE'])
    def delete_character(id): 
      pass 

    @app.route('/characters/<int:id>', methods=['PUT'])
    def update_artist(id): 
      pass 

    @app.route('/comics/<int:id>/characters', methods=['GET'])
    def get_characters_in_comic(id): 
      characters = [character.to_dict() for character in Comic.query.get(id).characters]
      return jsonify(characters)
            
    return app 

from app.models import Comic, Character
