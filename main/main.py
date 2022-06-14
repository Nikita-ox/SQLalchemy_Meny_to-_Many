from flask import Flask, request
from flask_restx import Api, Resource
from flask_sqlalchemy import SQLAlchemy
from marshmallow import Schema, fields

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///genre.db"  # "sqlite:///:memory:"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


class Author_Book(db.Model):
    __tablename__ = 'author_book'
    id = db.Column(db.Integer, primary_key=True)
    author_id = db.Column(db.Integer(), db.ForeignKey("authors.id"))
    book_id = db.Column(db.Integer(), db.ForeignKey("books.id"))


class Author(db.Model):
    __tablename__ = 'authors'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    books = db.relationship("Author_Book", backref='author')


class Book(db.Model):
    __tablename__ = 'books'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100))
    authors = db.relationship("Author_Book", backref="book")
    genre_id = db.Column(db.Integer, db.ForeignKey('genre.id'))

    genre = db.relationship("Genre")

    def __repr__(self):
        return self.name


class Genre(db.Model):
    __tablename__ = 'genre'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))

    books = db.relationship("Book", back_populates="genre")


db.drop_all()
db.create_all()

genre_1 = Genre(id=1, name="Ужасы")
genre_2 = Genre(id=2, name="Роман")
genre_3 = Genre(id=3, name="Повесть")
genre_4 = Genre(id=4, name="Фантастика")
genres_all = [genre_1, genre_2, genre_3, genre_4]
with db.session.begin():
    db.session.add_all(genres_all)
    db.session.commit()

books_1 = Book(id=1, title="Вий", genre=genre_1)
books_2 = Book(id=2, title="Война и Мир", genre=genre_2)
books_3 = Book(id=3, title="Маленький принц", genre=genre_3)
books_4 = Book(id=4, title="Эпоха мертвых", genre=genre_1)
books_5 = Book(id=5, title="Земля лишних", genre=genre_4)
books_6 = Book(id=6, title="Стальная крыса", genre=genre_4)
books_all = [books_1, books_2, books_3, books_4, books_5, books_6]

with db.session.begin():
    db.session.add_all(books_all)
    db.session.commit()

authors_1 = Author(id=1, name="Н.В.Гоголь")
authors_2 = Author(id=2, name="Л.Н.Толстой")
authors_3 = Author(id=3, name="А.Д.Экзюпери")
authors_4 = Author(id=4, name="А.Ю.Круз")
authors_5 = Author(id=5, name="А.Ю.Круз")
authors_6 = Author(id=6, name="М.Круз")
authors_7 = Author(id=7, name="Г.Гарисон")
authors_all = [authors_1, authors_2, authors_3, authors_4, authors_5, authors_6, authors_7]

with db.session.begin():
    db.session.add_all(authors_all)
    db.session.commit()

author_book_1 = Author_Book(book_id=1, author_id=1)
author_book_2 = Author_Book(book_id=2, author_id=2)
author_book_3 = Author_Book(book_id=3, author_id=3)
author_book_4 = Author_Book(book_id=4, author_id=4)
author_book_5 = Author_Book(book_id=5, author_id=5)
author_book_6 = Author_Book(book_id=5, author_id=6)
author_book_7 = Author_Book(book_id=6, author_id=7)
author_book_all = [author_book_1, author_book_2, author_book_3, author_book_4, author_book_5, author_book_6,
                   author_book_7]

with db.session.begin():
    db.session.add_all(author_book_all)
    db.session.commit()
