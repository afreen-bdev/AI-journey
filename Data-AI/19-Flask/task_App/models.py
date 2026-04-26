from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Task(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200))
    urgency = db.Column(db.Integer)
    time_required = db.Column(db.Integer)
    priority = db.Column(db.String(50))