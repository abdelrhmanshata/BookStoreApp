from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, TextAreaField
from wtforms.validators import DataRequired
from flask_wtf.file import FileField, FileAllowed
from wtforms_sqlalchemy.fields import QuerySelectField
from myapp.models import Category


class BookForm(FlaskForm):
    title = StringField('Title', validators=[DataRequired()])
    details = TextAreaField('Details', validators=[DataRequired()])
    image = FileField("Image", validators=[FileAllowed(['jpg', 'png', 'jpeg'], 'Images only!') ])
    pages = IntegerField("Pages", validators=[DataRequired()])
    price = IntegerField("Price", validators=[DataRequired()])
    category_id = QuerySelectField("Category", query_factory=lambda: Category.get_all_categories())
