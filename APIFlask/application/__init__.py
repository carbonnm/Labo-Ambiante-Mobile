from flask import Flask
from flask import json
from flask import jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_socketio import SocketIO
from config import Config

def initDB():
    """
    Initialisation of the database.
    """
    db.create_all()

    db.session.commit()


app = Flask(__name__)
app.config.from_object(Config)

# Database part :
db = SQLAlchemy(app)

# Socket parts :
socketio = SocketIO(app)

from application import routes
from application import models

initDB()