from datetime import datetime, timedelta
from flask import request, jsonify

from server import app, db, ADMINS
from ..auth import jwt_required
import jwt

from src.schemas import UserSchema
from src.models import Users, Notes

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

    except:
        return jsonify({'error': 'Este usuário já existe'}), 200


@app.route('/users/<int:id>', methods=['GET'])
@jwt_required
def get_user(current_user, id):
    try:
        user = Users.query.get(id)
        user_dict = user_schema.dump(user)

        return jsonify({'User': user_dict}), 200

    except:
        return jsonify({'message': 'User Not Found'}), 404


@app.route('/users', methods=['GET'])
@jwt_required
def get_all_users(current_user):
    try:
        users = Users.query.all()
        users_dict = users_schema.dump(users)

        return jsonify({'Users': users_dict}), 200

    except:
        return jsonify({'message': 'Not Found'}), 404


@app.route('/users/<int:id>', methods=['PUT'])
@jwt_required
def update_user(current_user, id):
    try:
        user_auth = user_schema.dump(current_user)

        if user_auth['id'] == id or user_auth['email'] in ADMINS:
            email = request.json['email']
            password = request.json['password']

            user = Users.query.get(id)
            user.email = email
            user.password = password
            db.session.commit()

            return jsonify({'message': 'Usuário atualizado com sucesso'}), 200

        return jsonify({"error": "Você não tem permissão para ATUALIZAR este usuário."}), 403

    except:
        return jsonify({'message': 'Unknown error'}), 500


@app.route('/users/<int:id>', methods=['DELETE'])
@jwt_required
def delete_user(current_user, id):
    try:
        user_auth = user_schema.dump(current_user)

        if user_auth['id'] == id or user_auth['email'] in ADMINS:
            user = Users.query.get(id)
            notes = Notes.query.filter_by(user_id=user.id).all()

            for note in notes:
                db.session.delete(note)

            db.session.delete(user)
            db.session.commit()

            return jsonify({'message': 'Usuário deletado com sucesso'}), 200

        return jsonify({"error": "Você não tem permissão para DELETAR este usuário."}), 403

    except:
        return jsonify({'message': 'Unknown error'}), 500


@app.route('/login', methods=['POST'])
def login():
    try:
        email = request.json['email']
        pwd = request.json['password']

        user = Users.query.filter_by(email=email).first_or_404()
    except:
        return jsonify({'error': '''Usuário não encontrado. Verifique se seu email foi digitado corretamente.'''}), 404

    # Se não achar o usuario ou não foi passado a senha correta então da erro 403
    if not user or not user.check_password(pwd):
        return jsonify({'error': 'As suas credênciais estão erradas!'}), 403

    payload = {
        "id": user.id,
        # O TOKEN TEM DURAÇÃO DE 30 MINUTOS // Caso não queira isto então remova esta linha abaixo
        "exp": datetime.utcnow() + timedelta(minutes=30)
    }

    token = jwt.encode(payload, app.config['SECRET_KEY'], algorithm="HS256")

    return jsonify({"token": token})
