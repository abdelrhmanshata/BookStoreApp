from flask import render_template, request, redirect, url_for
from myapp.models import Book, db
# you write view functions
from myapp.books import book_blueprint
from myapp.books.forms import BookForm


@book_blueprint.route("", endpoint="home")
def home():
    books = Book.get_all_objects()
    # render data to the template
    return render_template("books/home.html", books=books)


@book_blueprint.route("/show/<int:id>", endpoint="show")
def show_book(id):
    book = Book.get_book_by_id(id)
    if book:
        return render_template("books/show_book.html", book=book)


@book_blueprint.route("/add", methods=["GET", "POST"], endpoint="add")
def add_book():
    if request.method == "POST":
        book = Book.save_book(request.form, request.files)
        return redirect("/")
        # return redirect(book.show_url)
    return render_template("books/add_book.html")


@book_blueprint.route("/addByForm", methods=["GET", "POST"], endpoint="addByForm")
def add_book_by_form():
    form = BookForm(request.form)
    if request.method == 'POST':
        if "csrf_token" not in request.form.keys():
            return "error", 419
        if form.validate():
            bookData = dict(request.form)
            del bookData['csrf_token']
            book = Book.save_book(bookData, request.files)
            return redirect(url_for("books.home"))
    return render_template("books/add_book_by_form.html", form=form)

@book_blueprint.route("/updateByForm", methods=["GET", "POST"], endpoint="updateByForm")
def update_book_by_form():
    book = Book.query.get_or_404(id)
    form = BookForm(book)
    if request.method == 'POST':
        if "csrf_token" not in request.form.keys():
            return "error", 419
        if form.validate():
            bookData = dict(request.form)
            del bookData['csrf_token']
            book = Book.save_book(bookData, request.files)
            return redirect(url_for("books.home"))
    return render_template("books/add_book_by_form.html", form=form)


@book_blueprint.route("/update/<int:id>", endpoint="update", methods=["GET", "POST"])
def update_book(id):
    book = Book.query.get_or_404(id)
    if request.method == "POST":
        Book.update_book(book, request.form, request.files)
        return redirect("home")
    else:
        if book:
            return render_template("books/update_book.html", book=book)
    return render_template("error/error.html")


@book_blueprint.route("/delete/<int:id>", endpoint="delete", methods=["GET"])
def delete_book(id):
    book = Book.query.get_or_404(id)
    if book:
        Book.delete_book_by_id(id)
        return redirect("home")
    error = "Book Not Found"
    return render_template("error/error.html", error=error)


@book_blueprint.errorhandler(404)
def get_404(error):
    return render_template("error/error.html", error=error)
