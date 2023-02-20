from flask import request, jsonify
from functools import wraps

from models import Users
from server import app
import jwt


def jwt_required(f):
    @wraps(f)
    def wrapper(*args, **kwargs):
        token = None

        if 'authorization' in request.headers:
            token = request.headers['authorization']

        if not token:
            return jsonify({"error": "Você não tem permissão para acessar esta rota."}), 403

        if not 'Bearer' in token:
            return jsonify({"error": "token inválido."}), 401

        try:
            token_limpo = token.replace('Bearer ', '')
            decoded = jwt.decode(
                token_limpo, app.config['SECRET_KEY'], algorithms='HS256')
            current_user = Users.query.get(decoded['id'])
        except:
            return jsonify({"error": "O token é inválido."}), 401

        return f(current_user=current_user, *args, **kwargs)

    return wrapper
