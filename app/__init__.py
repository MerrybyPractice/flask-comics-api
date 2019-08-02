from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from config import Config

db = SQLAlchemy() 
migrate = Migrate() 

def create_app(ConfigClass): 

  app = Flask(__name__)
  app.config.from_object(ConfigClass) 

  db.init_app(app) 
  migrate.init_app(app, db) 

  from app.api import bp as api_bp
  app.register_blueprint(api_bp, url_prefix='/api/v1')

  return app 

from app.models import Comic, Character
