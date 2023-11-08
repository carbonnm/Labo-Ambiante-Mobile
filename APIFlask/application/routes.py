from application import app
from application import db

from flask import render_template
from flask import redirect
from flask import url_for
from flask import request
from flask import flash
from flask import jsonify

from werkzeug.exceptions import abort

from application.models import *
from werkzeug.security import check_password_hash


@app.errorhandler(404)
def page_not_found(e):
    """
    Handler of the errors.
    Display 404 error whenever a page is not found
    """
    return jsonify({'error': '404 error'})

@app.errorhandler(500)
def server_error(e):
    """
    Handler of the errors.
    Display 500.html whenever a server error occures.
    """
    return jsonify({'error': '500 error'})

@app.route("/")
def homepage():
    """
    Main page.
    Redirection to the home page
    """
    return jsonify({'data' : 'hello'})