## Models permet de definir les données de l app

from .app import db
from flask_login import UserMixin
from .app import login_manager
class Author(db.Model):
    id = db.Column(db.Integer, primary_key =True)
    name = db.Column(db.String(100))
    def __repr__(self):
        return "<Author (%d) %s>" % (self.id, self.name)
class Book(db.Model ):
    id = db.Column(db.Integer, primary_key =True)
    price = db.Column(db.Float)
    title = db.Column(db.String(500))
    url = db.Column(db.String(200))
    img = db.Column(db.String(100))
    # relation pour avoir les auteurs d un livre
    author_id = db.Column(db.Integer, db.ForeignKey("author.id"))
    # relation inverse pour avoir les livres d un auteur
    author = db.relationship("Author",
        backref=db.backref("books", lazy="dynamic"))
    def __repr__ (self ):
        return "<Book (%d) %s>" % (self.id, self.title)

class User(db.Model , UserMixin ):
    username = db.Column(db.String(50) , primary_key=True)
    password = db.Column(db.String(64))
    
    def get_id(self ):
        return self.username

def get_books():
    return Book.query.all()
def get_author(id):
    return Author.query.get(id)
def get_authors():
    return Author.query.all()

@login_manager.user_loader
def load_user(username):
    return User.query.get(username)