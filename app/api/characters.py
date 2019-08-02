from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from config import Config
from app import db
from app.models import Character
from app.models import Comic

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
  character = character.query.get(id) 
  db.session.delete(character) 
  db.session.commit()
  return 'Comic has been removed' 

@app.route('/characters/<int:id>', methods=['PUT'])
def update_artist(id): 
  character_info = request.json or request.form or request.values
  character = Character.query.get(id) 
  character.update(character_info)
  db.session.commit()
  return 'Character has been updated'

@app.route('/comics/<int:id>/characters', methods=['GET'])
def get_characters_in_comic(id): 
  characters = [character.to_dict() for character in Comic.query.get(id).characters]
  return jsonify(characters)
            
