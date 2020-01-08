import csv
from flask import Flask, session, redirect, render_template, flash, url_for
from flask_login import LoginManager, UserMixin, login_user, login_required
from flaskForm.form import AdminLogin
from appHelperFunctions import check_password
app = Flask(__name__)
app.secret_key = 'ahvuitrx68x68457f9876'

login_manager = LoginManager()
login_manager.init_app(app)

# without setting the login_view, attempting to access @login_required endpoints will result in an error
# this way, it will redirect to the login page
login_manager.login_view = '/'
app.config['USE_SESSION_FOR_NEXT'] = True


class User(UserMixin):
    def __init__(self, Username):
        self.id = Username


# this is used by flask_login to get a user object for the current user
# since we don't have any user information besides the user name,
# we just create a basic User object from the class above
# the next version will improve on this
@login_manager.user_loader
def load_user(user_id):
    return User(user_id)


@app.route('/', methods=['GET', 'POST'])
def homePage():
    with open("./data/hub-list.csv") as f:
        listItems = list(csv.reader(f))[0:]
    form = AdminLogin()
    if form.validate_on_submit():
        if check_password(form.Username.data, form.Password.data):
            login_user(User(form.Username.data))
            flash('Logged in successfully.')
            session['Username'] = form.Username.data

            # check if the next page is set in the session by the @login_required decorator
            # if not set, it will default to '/'
            next_page = session.get('next', '/')
            # reset the next page to default '/'
            session['next'] = '/'
            return redirect(next_page)
        else:
            flash('Incorrect username/password!')
            return redirect(url_for('homePage'))
    return render_template('homePage.html', listItems=listItems, form=form, username=session.get('Username'))



@app.route('/maps')
def maps():
    form = AdminLogin()
    with open("./data/map-names.csv") as f:
        listName = list(csv.reader(f))[0:]
    return render_template('maps.html', listName=listName, form=form, username=session.get('Username'))


@app.route('/construction')
@login_required
def construction():
    form = AdminLogin()
    return render_template('construction.html', form=form, username=session.get('Username'))


@app.route('/character')
def character():
    with open("./data/attributeTable.csv") as f:
        table = list(csv.reader(f))[0:]
    form = AdminLogin()
    return render_template('character.html', table=table, form=form, username=session.get('Username'))


@app.route('/anorLondo')
def anarLondo():
    form = AdminLogin()
    return render_template('anorLondo.html', form=form, username=session.get('Username'))


@app.route('/logout')
@login_required
def logout():
    session.clear()
    return redirect('/')


if __name__ == '__main__':
    app.run()
