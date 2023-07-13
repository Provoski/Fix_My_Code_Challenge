#!/usr/bin/python3
""" Index view
"""
from flask import jsonify, Blueprint, Flask

app_views = Blueprint('app_views', __name__)
app = Flask(__name__)
app.register_blueprint(app_views)

@app_views.route('/api/v1/status', methods=['GET'])
def status():
    """ Status of the web server
    """
    return jsonify({"status": "OK"})


if __name__ == '__main__':
    app.run();
