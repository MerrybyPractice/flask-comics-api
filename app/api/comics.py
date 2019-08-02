from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from config import Config
from app import db
from app.models import Comic


@app.route('/comics', methods=['GET'])
def all_comics(): 
  comics = [comic.to_dict() for comic in Comic.query.all()] 
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
  comic = Comic.query.get(id) 
  db.session.delete(comic) 
  db.session.commit()
  return 'Comic has been removed'

@app.route('/comics/<int:id>', methods=['PUT'])
def  update_comic(id): 
  comic_info = request.json or request.form or request.values
  comic = Comic.query.get(id) 
  comic.update(comic_info)
  db.session.commit()
  return 'Comic has been updated'