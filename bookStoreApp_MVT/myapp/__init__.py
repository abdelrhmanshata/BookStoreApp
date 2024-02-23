from flask import Flask
from myapp.config import AppConfig
from myapp.models import db
from flask_migrate import Migrate
from flask_restful import Api


def create_app(config_name="prd"):
    # create app
    app = Flask(__name__)
    current_config = AppConfig[config_name]
    print(current_config)
    ## read database configuration from config class
    app.config["SQLALCHEMY_DATABASE_URI"] = current_config.SQLALCHEMY_DATABASE_URI
    # app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    app.config["UPLOAD_FOLDER"] = (
        current_config.UPLOAD_FOLDER
    )  # Folder to store uploaded images

    app.config.from_object(current_config)
    # define db to the app
    db.init_app(app)

    ## init migration
    migrate = Migrate(app, db, render_as_batch=True)

    # add url
    from myapp.books.views import home

    app.add_url_rule("/", view_func=home, endpoint="landing")

    # create architecture // views , templates
    # introduce  blueprint to the application
    from myapp.books import book_blueprint
    app.register_blueprint(book_blueprint)

    from myapp.category import category_blueprint
    app.register_blueprint(category_blueprint)

    ### we need to add the API urls
    api = Api(app)  # generate apis for this project
    # add the class book resource to the api
    from myapp.books.viewsApi import BookList, BookResource
    api.add_resource(BookList, '/api/books')
    api.add_resource(BookResource, '/api/books/<int:book_id>')

    return app
