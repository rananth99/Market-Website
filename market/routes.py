from market import app
from flask import render_template, redirect, url_for, flash
from market import db
from market.models import Item, User
from market.forms import RegisterForm, LoginForm


@app.route("/")
@app.route("/home")
def home_page():
    return render_template('home.html')


@app.route("/market")
def market_page():
    items = Item.query.all()
    return render_template('market.html', items=items)


@app.route("/register", methods=['GET', 'POST'])
def register_page():
    form = RegisterForm()
    if form.validate_on_submit():
        user_to_create = User(
            username=form.username.data,
            email_address=form.email_address.data,
            password=form.password.data
        )
        db.session.add(user_to_create)
        db.session.commit()
        return redirect(url_for('market_page'))

    if form.errors != {}:
        for err_msg in form.errors.values():
            flash(
                f'There was an error creating the user : {err_msg[0]}', category='danger'
            )
    return render_template('register.html', form=form)


@app.route("/login", methods=["GET", "POST"])
def login_page():
    form = LoginForm()
    if form.validate_on_submit():
        user_to_login = User(username=form.usrename.data,
                             password=form.password.data)
    return render_template('login.html', form=form)
