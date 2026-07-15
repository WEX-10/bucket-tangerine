# TASKS P1.2, P4.5

from flask import render_template, request
from database import create_fact

def create_route():
    if request.method == "GET":
        # TODO: (Task P1.2) Render the create.html template
        render_template("create.html")
        pass

    if request.method == "POST":
        # TODO: (Task P1.2) Get the fact_text from the form
        factt = request.form.get("fact_text")

        # TODO: (Task P4.5) Get the category from the form

        # TODO: (Task P1.2) Check that fact text is provided, if not return an error
        if factt == None:
            raise ValueError("No Fact Provided by Users")
        # TODO: (Task P1.2) Call the create_fact function from the database folder
        fact = create_fact(factt)
        if fact.id == None:
            raise ValueError("No Fact Provided by Database")
        # TODO: (Task P4.5) Pass the category to the create_fact function

        return render_template("create.html", random_fact=factt) # TODO: (Task P1.2) Pass the HTML template, fact and category (Task P4.5) parameters
