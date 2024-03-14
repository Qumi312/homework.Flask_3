from flask import Flask, render_template, request, redirect, url_for, session

from forms import RegForm, LogForm
from models import db, User

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///mydatabase.db'
app.config['SECRET_KEY'] = 'asdfasdfasdfasdfasdf'
db.init_app(app)


@app.cli.command('init-db')
def init_db():
    db.create_all()


@app.route('/index/')
def index():
    if 'email' in session:
        return f'Привет{session["firstname"]}'
    else:
        return redirect(url_for('login'))


@app.route('/reg/', methods=['GET', 'POST'])
def reg():
    form = RegForm()
    if request.method == 'POST' and form.validate_on_submit():
        new_user = User(
            firstname=form.firstname.data,
            lastname=form.lastname.data,
            email=form.email.data,
            password=form.password.data,
            confirm_password=form.confirm_password.data,
        )
        db.session.add(new_user)
        db.session.commit()
        return redirect(url_for('login'))
    return render_template('reg.html', form=form)


@app.route('/logout/')
def logout():
    session.pop('email', None)
    return redirect(url_for('login'))


@app.route('/login/', methods=['GET', 'POST'])
def login():
    form = LogForm()
    if request.method == 'POST' and form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user is not None and user.password ==form.password.data:
            session["email"] = User.query.filter_by(email=form.email.data).first()
            return redirect(url_for('index'))
    return render_template('login.html', form=form)


if __name__ == '__main__':
    app.run()
