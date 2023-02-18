from flask import request, jsonify
from server import app, db

from src.schemas import UserSchema
from src.models import Users, Posts

user_schema = UserSchema()
users_schema = UserSchema(many=True)


@app.route('/register', methods=['POST'])
def create_user():
    try:
        email = request.json['email']
        password = request.json['password']

        new_user = Users(email=email, password=password)

        db.session.add(new_user)
        db.session.commit()

        return jsonify({'message': 'Usuário criado com sucesso'}), 200

    except Exception as error:
        return jsonify({'message': error}), 500


@app.route('/users/<int:id>', methods=['GET'])
def get_user(id):
    try:
        user = Users.query.get(id)
        user_dict = user_schema.dump(user)

        return jsonify({'User': user_dict}), 200

    except:
        return jsonify({'message': 'User Not Found'}), 404


@app.route('/users', methods=['GET'])
def get_all_users():
    try:
        users = Users.query.all()
        users_dict = users_schema.dump(users)

        return jsonify({'Users': users_dict}), 200

    except:
        return jsonify({'message': 'Not Found'}), 404


@app.route('/users/<int:id>', methods=['PUT'])
def update_user(id):
    try:
        user = Users.query.get(id)
        email = request.json['email']
        password = request.json['password']

        user.email = email
        user.password = password
        db.session.commit()

        return jsonify({'message': 'Usuário atualizado com sucesso'}), 200

    except Exception as error:
        return jsonify({'message': error}), 500


@app.route('/users/<int:id>', methods=['DELETE'])
def delete_user(id):
    try:
        user = Users.query.get(id)
        posts = Posts.query.filter_by(user_id=user.id).all()

        for post in posts:
            db.session.delete(post)

        db.session.delete(user)
        db.session.commit()

        return jsonify({'message': 'Usuário deletado com sucesso'}), 200

    except Exception as error:
        return jsonify({'message': error}), 500
