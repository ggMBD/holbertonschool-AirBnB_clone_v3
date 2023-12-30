#!/usr/bin/python3
"""
start web app
"""

from api.v1.views import app_views
from flask import jsonify


@app_views.route('/status')
def get_status():
    """Returns a JSON response with status OK."""
    return jsonify({"status": "OK"})
