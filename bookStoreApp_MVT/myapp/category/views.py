from flask import render_template, request, redirect, url_for
from myapp.category import category_blueprint
from myapp.models import Category
from myapp.category.forms import CategoryForm


@category_blueprint.route("/home", methods=['GET'], endpoint="categoryHome")
def categoryHome():
    categories = Category.get_all_categories()
    return render_template("category/home.html", categories=categories)


@category_blueprint.route("/addCategory", methods=["GET", "POST"], endpoint="addCategory")
def add_category_by_form():
    form = CategoryForm(request.form)
    if request.method == 'POST':
        if "csrf_token" not in request.form.keys():
            return "error", 419
        if form.validate():
            categoryData = dict(request.form)
            del categoryData['csrf_token']
            category = Category.save_category(categoryData)
            return redirect(url_for("category.categoryHome"))
    return render_template("category/add_category_by_form.html", form=form)


@category_blueprint.route("/updateCategory/<int:id>", methods=["GET", "POST"], endpoint="updateCategory")
def update_category_by_form(id):
    category = Category.get_category_by_id(id)
    print(category)
    form = CategoryForm(obj=category)
    if request.method == 'POST':
        if "csrf_token" not in request.form.keys():
            return "error", 419
        if form.validate():
            categoryData = dict(request.form)
            del categoryData['csrf_token']
            category = Category.update_category(category, categoryData)
            return redirect(url_for("category.categoryHome"))
    return render_template("category/update_category_by_form.html", form=form)


@category_blueprint.route("/deleteCategory/<int:id>", endpoint="delete", methods=["GET"])
def delete_category(id):
    category = Category.query.get_or_404(id)
    if category:
        Category.delete_category_by_id(id)
        return redirect(url_for("category.categoryHome"))
    error = "Category Not Found"
    return render_template("error/error.html", error=error)
