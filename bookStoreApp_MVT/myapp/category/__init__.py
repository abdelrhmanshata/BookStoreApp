"""
    you need to connect the view function with the app
    we can implement using blueprint
"""
# each application has its own blue pring
from flask import Blueprint
# create blueprint for the app
category_blueprint = Blueprint("category", __name__, url_prefix="/category")
# then you need to define the views that will use the blueprint
from myapp.category import views