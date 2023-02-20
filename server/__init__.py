from flask_marshmallow import Marshmallow
from flask_sqlalchemy import SQLAlchemy
from flask import Flask
import dotenv
import os

# COLETANDO AS VARIÁVEIS DO ARQUIVO .ENV
dotenv.load_dotenv(dotenv.find_dotenv())
DATABASE = os.getenv("DATABASE")
SECRET_KEY = os.getenv("SECRET_KEY")
ADMINS = os.getenv("ADMINS")

# CRIANDO E CONFIGURANDO INSTÂNCIA DO SERVIDOR
app = Flask(__name__)

# ESTE app SERÁ CHAMADO E INICIADO NO ARQUIVO main.py JUNTO COM OS CONTROLLERS
app.config['SQLALCHEMY_DATABASE_URI'] = DATABASE
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['PROPAGATE_EXCEPTIONS'] = True
app.config['SECRET_KEY'] = SECRET_KEY

# O SQLAlchemy NOS AJUDA MANIPULAR O BANCO DE DADOS SEM PRECISAR USAR SQL
db = SQLAlchemy(app)
# O Marshmallow FACILITA SERIALIZAR JSON NAS RESPONSE
ma = Marshmallow(app)
