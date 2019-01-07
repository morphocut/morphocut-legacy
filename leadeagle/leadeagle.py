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

from flask.helpers import send_from_directory
from sqlalchemy import func
from sqlalchemy.exc import IntegrityError
from sqlalchemy.sql.expression import bindparam
from sqlalchemy.sql import select, and_, union, intersect
from timer_cm import Timer
from werkzeug.security import check_password_hash, generate_password_hash
from werkzeug.utils import secure_filename

from leadeagle import models
from leadeagle.extensions import database, migrate, redis_store
from leadeagle.frontend import frontend
# from morphocluster.api import api
# from morphocluster.numpy_json_encoder import NumpyJSONEncoder
# from morphocluster.tree import Tree

# Enable fault handler for meaningful stack traces when a worker is killed
faulthandler.enable()

app = Flask(__name__)

app.config.from_object('leadeagle.config_default')
app.config.from_envvar('LEADEAGLE_SETTINGS')

# Initialize extensions
database.init_app(app)
redis_store.init_app(app)
migrate.init_app(app, database)
CORS(app)


# app.json_encoder = NumpyJSONEncoder

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


@app.route("/")
def index():
    print('index request')
    return redirect(url_for("frontend.index"))


@app.route('/ping', methods=['GET'])
def ping_pong():
    return jsonify('pong!')


@app.route('/datasets', methods=['GET', 'POST'])
def all_datasets():
    response_object = {'status': 'success'}
    if request.method == 'POST':
        post_data = request.get_json()
        if post_data is not None:
            # datasets.append({
            #     'id': post_data.get('id'),
            #     'name': post_data.get('name'),
            #     'objects': post_data.get('objects')
            # })
            add_dataset(post_data)
            response_object['message'] = 'Dataset added!'
    else:
        response_object['datasets'] = get_datasets()
    return jsonify(response_object)


@app.route('/upload', methods=['GET', 'POST', 'PUT'])
def upload():
    response_object = {'status': 'success'}
    print('upload '+str(request.method)+'\n')
    if request.method == 'POST':
        if 'file' not in request.files:
            flash('No file part')
            return redirect(request.url)
        file = request.files['file']
        dataset = json.loads(request.form['dataset'])
        print(str(dataset))
        # if user does not select file, browser also
        # submit an empty part without filename
        if file.filename == '':
            flash('No selected file')
            # return redirect(request.url)
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            _object = {
                'filename': os.path.join(app.config['UPLOAD_FOLDER'], filename),
                'dataset_id': dataset['id']
            }
            add_object(_object)
            print('save file')
            # return redirect(url_for('uploaded_file',
            #                         filename=filename))
    elif request.method == 'PUT':
        print('put put put')
    return jsonify(response_object)


def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower(
           ) in app.config['ALLOWED_EXTENSIONS']


def get_datasets():
    with database.engine.begin() as connection:
        result = connection.execute(select(
            [models.datasets.c.dataset_id, models.datasets.c.name, func.count(models.objects.c.object_id).label('object_count')])
            .select_from(models.datasets.outerjoin(models.objects))
            .where(models.datasets.c.active == True)
            .group_by(models.datasets.c.dataset_id))
        return [dict(id=row['dataset_id'], objects=row['object_count'], name=row['name']) for row in result]


def add_dataset(dataset):
    print('add_dataset: '+str(dataset))
    try_insert_or_update(models.datasets.insert(), [dict(
        name=dataset['name'], active=True)], "datasets")
    return


def add_object(_object):
    print('add_object: '+str(_object))
    try_insert_or_update(models.objects.insert(), [dict(
        dataset_id=_object['dataset_id'], filename=_object['filename'])], "objects")
    return


def try_insert_or_update(insert_function, data, table_name):
    """
    Try to insert a data list into the database
    """
    with database.engine.begin() as connection:
        if len(data) > 0:
            connection.execute(insert_function, data)


app.register_blueprint(frontend, url_prefix='/frontend')
