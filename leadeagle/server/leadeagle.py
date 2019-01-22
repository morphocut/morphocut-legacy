from flask_cors import CORS
from flask import jsonify
import faulthandler
import itertools
import os
from getpass import getpass
from time import sleep

import click
import flask_migrate
import h5py
import pandas as pd
from etaprogress.progress import ProgressBar
from flask import (Flask, Response, abort, redirect, render_template, request,
                   url_for)
import json
import urllib.parse

from flask.helpers import send_from_directory
import sqlalchemy
from sqlalchemy import func
from sqlalchemy.exc import IntegrityError
from sqlalchemy.sql.expression import bindparam
from sqlalchemy.sql import select, and_, union, intersect
from timer_cm import Timer
from werkzeug.security import check_password_hash, generate_password_hash
from werkzeug.utils import secure_filename

from leadeagle.server import models
from leadeagle import segmentation
from leadeagle.server.extensions import database, migrate, redis_store
from leadeagle.server.frontend import frontend
from leadeagle.server.api import api

# Enable fault handler for meaningful stack traces when a worker is killed
faulthandler.enable()

app = Flask(__name__)

app.config.from_object('leadeagle.server.config_default')

if 'LEADEAGLE_SETTINGS' in os.environ:
    app.config.from_envvar('LEADEAGLE_SETTINGS')

# Initialize extensions
database.init_app(app)
redis_store.init_app(app)
migrate.init_app(app, database)
CORS(app)


# Enable batch mode
with app.app_context():
    database.engine.dialect.psycopg2_batch_mode = True


@app.cli.command()
def reset_db():
    """
    Drop all tables and recreate.
    """
    print("Resetting the database.")
    print("WARNING: This is a destructive operation and all data will be lost.")

    if input("Continue? (y/n) ") != "y":
        print("Canceled.")
        return

    with database.engine.begin() as txn:
        database.metadata.drop_all(txn)
        database.metadata.create_all(txn)

        flask_migrate.stamp()


@app.cli.command('hello_cmd')
def hello_cmd():
    """
    Drop all tables and recreate.
    """
    print("hello")


# Register API and frontend
app.register_blueprint(frontend, url_prefix='/frontend')
app.register_blueprint(api, url_prefix='/api')


@app.route("/")
def index():
    print('index request')
    return redirect(url_for("frontend.index"))


# ===============================================================================
# Authentication
# ===============================================================================


def check_auth(username, password):
    # Retrieve entry from the database
    with database.engine.connect() as conn:
        stmt = models.users.select(
            models.users.c.username == username).limit(1)
        user = conn.execute(stmt).first()

        if user is None:
            return False

    return check_password_hash(user["pwhash"], password)


# @app.before_request
def require_auth():
    # exclude 404 errors and static routes
    # uses split to handle blueprint static routes as well
    if not request.endpoint or request.endpoint.rsplit('.', 1)[-1] == 'static':
        return

    auth = request.authorization

    success = check_auth(auth.username, auth.password) if auth else None

    if not auth or not success:
        if success is False:
            # Rate limiting for failed passwords
            sleep(1)

        # Send a 401 response that enables basic auth
        return Response(
            'Could not verify your access level.\n'
            'You have to login with proper credentials', 401,
            {'WWW-Authenticate': 'Basic realm="Login Required"'})
