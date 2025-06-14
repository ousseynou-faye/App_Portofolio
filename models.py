# from app import db
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Projet(db.Model):
    
    id = db.Column(db.Integer, primary_key=True)
    slug = db.Column(db.String(80), unique=True, nullable=False)
    title = db.Column(db.String(120), nullable=False)
    description = db.Column(db.Text, nullable=False)
    image = db.Column(db.String(120))
    tech = db.Column(db.String(200)) # Liste de technologies séparées par des virgules
    
    def get_tech_list(self):
        return self.tech.split(',')