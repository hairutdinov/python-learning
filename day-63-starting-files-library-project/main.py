from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///books-collection.db'

db = SQLAlchemy()
db.init_app(app)


class Book(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(250), unique=True, nullable=False)
    author = db.Column(db.String(250), nullable=False)
    rating = db.Column(db.Float, nullable=False)

@app.route('/')
def home():
    all_books = db.session.execute(db.select(Book)).scalars()
    print(all_books)
    print(dir(all_books))
    return render_template('index.html', books=all_books)


@app.route('/add', methods=['GET', 'POST'])
def add():
    if request.method == 'POST':
        new_book = Book(
            title=request.form.get('title'),
            author=request.form.get('author'),
            rating=request.form.get('rating'),
        )
        db.session.add(new_book)
        db.session.commit()
        return redirect(url_for('home'))
    return render_template('add.html')


@app.route('/edit-rating/<int:book_id>', methods=['GET', 'POST'])
def edit_rating(book_id):
    # book = db.session.execute(db.select(Book).where(Book.id == book_id)).scalar()
    book = db.get_or_404(Book, book_id)
    if request.method == 'POST':
        book.rating = request.form['rating']
        db.session.commit()
        return redirect(url_for('home'))
    return render_template('edit-rating.html', id=book_id, book=book)


@app.route('/delete')
def delete():
    book_id = request.args.get('id')
    book = db.get_or_404(Book, book_id)
    db.session.delete(book)
    db.session.commit()
    return redirect(url_for('home'))


with app.app_context():
    db.create_all()

if __name__ == '__main__':
    app.run(debug=True, port=8000)
