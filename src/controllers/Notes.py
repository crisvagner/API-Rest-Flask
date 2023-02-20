from flask import request, jsonify
from server import app, db

# IMPORTANDO FUNÇÃO DE PROTEÇÃO COM TOKEN JWT
from ..auth import jwt_required

from src.schemas import NoteSchema, UserSchema
from src.models import Notes

note_schema = NoteSchema()
notes_schema = NoteSchema(many=True)
user_schema = UserSchema()
users_schema = UserSchema(many=True)


@app.route('/notes', methods=['POST'])
@jwt_required
def create_post(current_user):
    try:
        user = user_schema.dump(current_user)

        title = request.json['title']
        content = request.json['content']

        new_note = Notes(title=title, content=content, user_id=user['id'])

        db.session.add(new_note)
        db.session.commit()

        return jsonify({'message': 'Tarefa criada com sucesso'}), 200

    except:
        return jsonify({'message': 'Unknown error'}), 500


@app.route('/notes/<int:note_id>', methods=['GET'])
@jwt_required
def get_post(current_user, note_id):
    try:
        user = user_schema.dump(current_user)

        note = Notes.query.filter_by(
            user_id=user['id'], id=note_id).first_or_404()
        note_dict = note_schema.dump(note)

        return jsonify({'Note': note_dict}), 200

    except:
        return jsonify({'message': 'Note Not Found'}), 404


@app.route('/notes', methods=['GET'])
@jwt_required
def get_all_posts(current_user):
    try:
        user = user_schema.dump(current_user)

        notes = Notes.query.filter_by(user_id=user['id']).all()
        notes_dict = notes_schema.dump(notes)

        return jsonify({'Notes': notes_dict}), 200

    except:
        return jsonify({'message': 'Not Found'}), 404


@app.route('/notes/<int:note_id>', methods=['PUT'])
@jwt_required
def update_post(current_user, note_id):
    try:
        user = user_schema.dump(current_user)

        note = Notes.query.filter_by(user_id=user['id']).get(note_id)

        title = request.json['title']
        content = request.json['content']

        note.title = title
        note.content = content
        db.session.commit()

        return jsonify({'message': 'Tarefa atualizada com sucesso'}), 200

    except:
        return jsonify({'message': 'Unknown error'}), 500


@app.route('/notes/<int:note_id>', methods=['DELETE'])
@jwt_required
def delete_post(current_user, note_id):
    try:
        user = user_schema.dump(current_user)

        note = Notes.query.filter_by(user_id=user['id']).get(note_id)

        db.session.delete(note)
        db.session.commit()

        return jsonify({'message': 'Tarefa deletada com sucesso'}), 200

    except:
        return jsonify({'message': 'Unknown error'}), 500
