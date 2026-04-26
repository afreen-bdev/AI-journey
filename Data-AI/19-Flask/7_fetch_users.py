from flask import Flask, jsonify
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'

db = SQLAlchemy(app)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))

@app.route('/users')
def get_users():
    users = User.query.all()
    data = [{"id": u.id, "name": u.name} for u in users]
    return jsonify(data)

if __name__ == '__main__':
    app.run(debug=True)