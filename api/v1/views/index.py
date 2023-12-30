#!/usr/bin/python3
"""
start web app
"""

from api.v1.views import app_views
from flask import jsonify
from models import storage


@app_views.route('/status')
def get_stats():
    """Returns the number of each object type in storage."""
    classes = storage.classes
    stats = {}

    for cls_name, cls in classes.items():
        cls_count = storage.count(cls_name)
        stats[cls_name] = cls_count

    return jsonify(stats)
