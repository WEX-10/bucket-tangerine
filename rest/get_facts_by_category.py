# TASK P5.4

from flask import jsonify
from database import get_facts_by_category

def get_facts_by_category_route():
    categories = None # TODO: (Task P5.4) Get the categories from the database using get_facts_by_category
    return jsonify({"categories": categories})