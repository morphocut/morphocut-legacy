"""
Frontend blueprint
"""

import datetime

from flask.blueprints import Blueprint

frontend = Blueprint("frontend", __name__,
                     static_folder="server/frontend/dist", static_url_path="")


@frontend.route("/")
@frontend.route("/p")
@frontend.route("/p/<path:path>")
def index(path=None):
    response = frontend.send_static_file('index.html')
    del response.headers['Expires']
    del response.headers['ETag']
    response.headers['Last-Modified'] = datetime.datetime.now()
    response.headers['Cache-Control'] = 'no-cache, no-store, must-revalidate'
    response.headers['Pragma'] = 'no-cache'
    print('new request')
    print(response.headers)
    return response
