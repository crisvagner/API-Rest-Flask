from flask import jsonify
from server import app, db


@app.before_first_request
def create_tables():
    db.create_all()


@app.route('/')
def index():
    return jsonify({'message': 'Not Found'}), 404


if __name__ == '__main__':
    app.run(
        port=5000,
        debug=True,
        host='0.0.0.0'
    )
