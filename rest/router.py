# Tasks P0.3, P1.3, P3.3, P5.5

from flask import Flask
from .home import home_route
from rest.get_fact import get_route
from rest.create_fact import create_route
# TODO: (Task P1.3) Import the create_route function from the create_fact module
# TODO: (Task P3.3) Import the vote_fact function from the vote_fact module
# TODO: (Task P5.5) Import the get_facts_by_category_route function from the get_facts_by_category module

def create_app():
    app = Flask(__name__,
                template_folder='../templates',
                static_folder='../static')

    app.add_url_rule("/", view_func=home_route, methods=["GET"])
    app.add_url_rule("/generate", view_func=get_route, methods=["GET"])
    app.add_url_rule("/create", view_func=create_route, methods=["GET", "POST"])
    # TODO: (Task P0.3) Add a URL rule for the generate route
    # TODO: (Task P1.3) Add a URL rule for the create route
    # TODO: (Task P3.3) Add a URL rule for the vote route
    # TODO: (Task P5.5) Add a URL rule for the get_facts_by_category route

    return app