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
from flask.helpers import send_from_directory
from sqlalchemy.exc import IntegrityError
from sqlalchemy.sql.expression import bindparam
from sqlalchemy.sql import select, and_, union, intersect
from timer_cm import Timer
from werkzeug.security import check_password_hash, generate_password_hash

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


def get_datasets():
    with database.engine.begin() as connection:
        result = connection.execute(select(
            [models.datasets.c.dataset_id, models.datasets.c.name, models.datasets.c.objects]).select_from(models.datasets))
        return [dict(id=row['dataset_id'], objects=row['objects'], name=row['name']) for row in result]


def add_dataset(dataset):
    try_insert_or_update(models.datasets.insert(), [dict(
        name=dataset['name'], dataset_id=dataset['id'], objects=dataset['objects'])], "datasets")
    return


def try_insert_or_update(insert_function, data, table_name):
    """
    Try to insert a data list into the database
    """
    with database.engine.begin() as connection:
        if len(data) > 0:
            connection.execute(insert_function, data)


# datasets = [
#     {
#         'id': 0,
#         'name': 'Christian',
#                 'objects': 327
#     },
#     {
#         'id': 1,
#         'name': 'Christian',
#                 'objects': 13
#     },
#     {
#         'id': 2,
#         'name': 'Christian',
#                 'objects': 2156
#     }
# ]


# Register api
# app.register_blueprint(api, url_prefix='/api')
app.register_blueprint(frontend, url_prefix='/frontend')
