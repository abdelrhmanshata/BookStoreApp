import os
from flask_sqlalchemy import SQLAlchemy
from flask import url_for
from datetime import datetime
from werkzeug.utils import secure_filename

db = SQLAlchemy()
class Book(db.Model):
    __tablename__ = "books"
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String)
    details = db.Column(db.String)
    pages = db.Column(db.Integer)
    price = db.Column(db.Integer)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    update_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    image = db.Column(db.String, default="book.png")

    def __str__(self):
        return f"{self.id}/{self.title}/{self.details}/{self.pages}/{self.price}/{self.image}"

    @property
    def image_url(self):
        return url_for("static", filename=f"bookImages/{self.image}")

    @property
    def show_url(self):
        return url_for("book.show", id=self.id)

    @classmethod
    def get_all_objects(cls):
        return cls.query.all()

    @classmethod
    def get_book_by_id(cls, id):
        return cls.query.get_or_404(id)

    @classmethod
    def delete_book_by_id(cls, id):
        book = cls.query.get_or_404(id)
        db.session.delete(book)
        db.session.commit()
        return "Done"

    @classmethod
    def save_book(cls, request_data,request_files):  # immutable dict
        book = cls(**request_data)
        book.pages = int(book.pages)
        book.price = int(book.price)
        image = request_files["image"]
        if image:
            imageName = secure_filename(image.filename)
            image.save(os.path.join("D:\\Project\\Python\\bookStoreApp_MVT\\myapp\\static\\bookImages\\", imageName))
            book.image = imageName
        db.session.add(book)
        db.session.commit()
        return book

    @classmethod
    def update_book(cls,book, request_data,request_files):  # immutable dict
        bookObj = cls(**request_data)
        book.title = bookObj.title
        book.details = bookObj.details
        book.pages = int(bookObj.pages)
        book.price = int(bookObj.price)
        image = request_files["image"]
        if image:
            imageName = secure_filename(image.filename)
            image.save(os.path.join("D:\\Project\\Python\\bookStoreApp_MVT\\myapp\\static\\bookImages\\", imageName))
            book.image = imageName
        db.session.commit()
        return book