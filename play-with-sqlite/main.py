from flask import Flask
from flask_sqlalchemy import SQLAlchemy

# import sqlite3
#
#
# db = sqlite3.connect('books-collection.db')
# cursor = db.cursor()
#
# # cursor.execute("CREATE TABLE books"
# #                "(id INTEGER PRIMARY KEY,"
# #                "title varchar(250) NOT NULL UNIQUE,"
# #                "author varchar(250) NOT NULL,"
# #                "rating FLOAT NOT NULL)")
#
# cursor.execute("INSERT INTO books VALUES (1, 'Harry Potter', 'J. K. Rowling', 9.3)")
# db.commit()

app = Flask(__name__)

db = SQLAlchemy()
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///books-collection.db'
db.init_app(app)


class Books(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(250), unique=True, nullable=False)
    author = db.Column(db.String(250), nullable=False)
    rating = db.Column(db.Float, nullable=False)


# Create table schema in the database. Requires application context.
with app.app_context():
    db.create_all()

# CREATE
# with app.app_context():
#     book = Books(
#         title='Tale of Two Cities 2',
#         author='Charles Dickens',
#         rating=7
#     )
#     db.session.add(book)
#     db.session.commit()

# SELECT
# with app.app_context():
#     result = db.session.execute(db.select(Books)).scalars()
#     print(dir(result))
#     print(result.fetchall()[0])

# UPDATE
# with app.app_context():
#     book = db.session.execute(db.select(Books).where(Books.id == 1)).scalar()
#     book.title = 'Harry Potter and the Goblet of Fire'
#     db.session.commit()

# DELETE
# with app.app_context():
#     book = db.session.execute(db.select(Books).where(Books.id == 2)).scalar()
#     db.session.delete(book)
#     db.session.commit()
