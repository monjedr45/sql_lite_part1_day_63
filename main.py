from flask import Flask, render_template, request, redirect, url_for
from flask_bootstrap import Bootstrap
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectField
from wtforms.validators import DataRequired, URL

app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
Bootstrap(app)


class CafeForm(FlaskForm):
    book_name = StringField('book name', validators=[DataRequired()])
    book_author = StringField('book author', validators=[DataRequired()])
    rating = StringField('rating', validators=[DataRequired()])
    submit = SubmitField('submit')

all_books = []


@app.route('/')
def home():
    
    return render_template('index.html', books = all_books)


@app.route("/add", methods=['GET', 'POST'])
def add():
    form = CafeForm()
    if form.validate_on_submit():
        Book_name = form.book_name.data
        Author_name = form.book_author.data
        Rating = form.rating.data
        print(Book_name, Author_name, Rating)
        data__ =[
            {          
                "name":Book_name,
                "auther":Author_name,
                "rating":Rating},
        ]
        all_books.append(data__)
        
    return render_template('add.html', form=form)


if __name__ == "__main__":
    app.run(debug=True)

