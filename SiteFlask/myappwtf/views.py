##views permet de definir les routes de l app donc des differents pages

from .app import app,db
from flask import render_template, request,url_for , redirect
from .models import get_books,get_author,get_authors
from .models import Author,Book,User
from flask_wtf import FlaskForm
from wtforms import StringField , HiddenField,PasswordField
from wtforms.validators import DataRequired
from hashlib import sha256
from flask_login import login_user , current_user,logout_user

class AuthorForm(FlaskForm):
    id = HiddenField("id")
    name = StringField("Nom",validators=[DataRequired()])
class LoginForm ( FlaskForm ):
    username = StringField("Username")
    password = PasswordField("Password")
    next = HiddenField()
    def get_authenticated_user(self):
        user = User.query.get(self.username.data)
        if user is None:
            return None
        m = sha256()
        m. update(self.password.data.encode())
        passwd = m.hexdigest()
        return user if passwd == user.password else None

@app.route("/")
def home():
    return render_template(
        "home.html",
        title="My Books !",
        books=get_books(),authors=get_authors())
@app.route("/detail/<id>")
def detail(id):
    books = get_books()
    book = books[int(id)-1]
    return render_template(
    "detail.html",
    book=book)

@app.route ("/edit/author/<int:id>")
def edit_author(id):
    fl= LoginForm ()
    user=fl.get_authenticated_user()
    if user is None:
        next=url_for("edit_author",id=id)
        return redirect(url_for("login",next=next))
    a = get_author(id)
    f = AuthorForm (id=a.id , name=a.name)
    return render_template (
        "edit-author.html",
        author =a, form=f)
@app.route("/detail/author/<int:id>")
def detail_author(id):
    if id is None:
        return render_template("add-author.html",form=AuthorForm())
    a = get_author(id)
    return render_template(
        "detail-author.html",
        author=a)

@app.route("/save/author/", methods =("POST",))
def save_author():
    a = None
    f = AuthorForm()
    #si c'est une modification
    if f.validate_on_submit():
        if f.id.data:
            a = get_author(f.id.data)
            a.name = f.name.data
            id=int(f.id.data)
            db.session.commit()
            return redirect(url_for("detail_author", id=a.id ))
        else:
            #recupere l'id du dernier auteur
            id =int(Author.query.order_by(Author.id.desc()).first().id) +1  
            a = Author(id=id,name=f.name.data)
            db.session.add(a)
            db.session.commit()
            return redirect(url_for("detail_author", id=a.id ))
    a = get_author(int(f.id.data))
    return render_template(
        "edit-author.html",
        author =a, form=f)

@app.route("/add/author/")
def add_author():
    return render_template("add-author.html",form=AuthorForm(id=None,name=None))

@app.route("/search/", methods =("POST",))
def search():
    #recupere la valeur du champ de recherche
    search = request.form.get("search")
    #recupere les livres dont le titre contient la valeur de recherche
    books = Book.query.filter(Book.title.like("%"+search+"%")).all()
    authors = Author.query.filter(Author.name.like("%"+search+"%")).all()
    return render_template( "search-result.html", books=books,authors=authors)

@app.route ("/login/", methods =("GET","POST",))
def login():
    f = LoginForm ()
    if not f.is_submitted():
        f.next.data = request.args.get("next")
    elif f.validate_on_submit ():
        user = f.get_authenticated_user()
        if user:
            login_user(user)
            next = f.next.data
            return redirect(next)
        
    return render_template (
    "login.html",
    form=f)
@app.route("/logout/")
def logout():
    logout_user()
    return redirect(url_for('home'))