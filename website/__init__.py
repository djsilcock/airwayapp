from flask import Flask
from flask_sqlalchemy import SQLAlchemy
db=SQLAlchemy()
from . import content,slack
def create_app():
  app=Flask('website')
  app.register_blueprint(content.blueprint,url_prefix='/')
  app.register_blueprint(slack.blueprint,url_prefix='/slack/')

  app.config.from_object("website.config")
  db.init_app(app)
  return app
  
  
