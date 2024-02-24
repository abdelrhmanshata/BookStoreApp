# define parser to convert request.data to python datatypes

from flask_restful import reqparse

book_parser = reqparse.RequestParser()
book_parser.add_argument('title', type=str, required=True, help="Title is required")
book_parser.add_argument('details', type=str)
book_parser.add_argument('pages', type=int)
book_parser.add_argument('price', type=int)
book_parser.add_argument('image', type=str)
book_parser.add_argument('category_id', type=int)
