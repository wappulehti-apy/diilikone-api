from flask import Blueprint, redirect, render_template, url_for
from flask_login import login_required, login_user, logout_user

from diilikone.admin.forms import LoginForm
from diilikone.models import User

admin_login = Blueprint('admin_login', __name__, url_prefix='/admin')


@admin_login.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user and user.password == form.password.data:
            print('oikeat kredentiaaalit')
            login_user(user, force=True)
            return redirect(url_for("deal.index_view"))
    return render_template("admin/login.html", form=form)


@admin_login.route("/logout")
@login_required
def logout():
    logout_user()
    return redirect(url_for("admin_login.login"))
