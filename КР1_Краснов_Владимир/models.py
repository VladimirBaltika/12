from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Note(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(1000000), nullable=False)
    description = db.Column(db.String(100000), nullable=True)