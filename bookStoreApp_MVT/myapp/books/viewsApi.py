from myapp.models import Book, db
from myapp.books import book_blueprint
from flask_restful import Resource, fields, marshal_with
from flask import request
from myapp.books.parsers import book_parser


@book_blueprint.route("/api", endpoint="homeAPI")
def home():
    books = Book.get_all_objects()
    booksList = []
    for book in books:
        book_data = book.__dict__
        del book_data["_sa_instance_state"]
        booksList.append(book_data)

    print(booksList)
    return booksList

category_serilizer = {
    "id": fields.Integer,
    "name": fields.String
}

book_serilizer = {
    "id": fields.Integer,
    "title": fields.String,
    "image": fields.String,
    "pages": fields.Integer,
    "price": fields.Integer,
    "category_id": fields.Integer,
    "category_name": fields.Nested(category_serilizer)
}


class BookList(Resource):
    @marshal_with(book_serilizer)
    def get(self):
        books = Book.query.all()
        return books, 200

    @marshal_with(book_serilizer)
    def post(self):
        book_data = book_parser.parse_args()
        book = Book.save_book(book_data)
        return book, 201


## crud operation on book // show , edit , delete
class BookResource(Resource):
    @marshal_with(book_serilizer)
    def get(self, book_id):
        book = Book.get_book_by_id(book_id)
        return book, 200

    @marshal_with(book_serilizer)
    def put(self, book_id):
        book = Book.get_book_by_id(book_id)
        if book:
            book_data = book_parser.parse_args()
            book.title = book_data["title"]
            book.details = book_data["details"]
            book.pages = book_data["pages"]
            book.price = book_data["price"]
            book.image = book_data["image"]
            book.category_id = book_data["category_id"]

            db.session.add(book)
            db.session.commit()
            return book

    def delete(self, book_id):
        deleted = Book.delete_book_by_id(book_id)
        return deleted, 204
