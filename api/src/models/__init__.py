from werkzeug.security import generate_password_hash, check_password_hash
from server import db


# MODEL DE USUÁRIO
class Users(db.Model):

    id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(120), nullable=False)
    posts = db.relationship('Tasks', backref='author', lazy=True)

    def __init__(self, email, password):
        self.email = email
        self.password = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password, password)

    def __repr__(self):
        return f'<User {self.email}>'


# MODEL DE TAREFAS
class Tasks(db.Model):
    id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    content = db.Column(db.Text, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)

    def __repr__(self):
        return f'<Task {self.title}>'
