from Bank import app
from flask import render_template, flash, url_for, redirect
from flask_login import login_user, logout_user, login_required, current_user
from Bank.forms import RegisterForm, LoginForm
from Bank.models import Customer
from Bank import db


@app.route('/')
@app.route('/home')
def home_page():
    return render_template('base.html')


@app.route('/register', methods=['GET', 'POST'])
def register_page():
    form = RegisterForm()
    if form.validate_on_submit():
        customer_to_create = Customer(first_name=form.first_name.data,
                                      last_name=form.last_name.data,
                                      mobileNumber=form.mobileNumber.data,
                                      address=form.address.data,
                                      city=form.city.data,
                                      state=form.state.data,
                                      password=form.password1.data,
                                      zip_code=form.zip_code.data
                                      )
        db.session.add(customer_to_create)
        db.session.commit()

        flash(f"Account created successfully! Welcome to our bank: {customer_to_create.first_name}",
              category='success')
        return redirect(url_for('home_page'))
    if form.errors != {}:
        for err_msg in form.errors.values():
            flash(f'Error while creating User: {err_msg}', category='danger')
    return render_template('register.html', form=form)


@app.route('/login', methods=['GET', 'POST'])
def login_page():
    form = LoginForm()
    if form.validate_on_submit():
        attempted_user = Customer.query.filter_by(mobileNumber=form.mobileNumber.data).first()
        if attempted_user and attempted_user.check_password_correction(attempted_password=form.password.data):
            login_user(attempted_user)
            flash(f'You are logged in as: {attempted_user.first_name}', category='success')
            return redirect(url_for('detail_page'))
        else:
            flash('Mobile Number and Password are not matched! Please insert valid credentials.', category='danger')
    return render_template('login.html', form=form)


@app.route('/detail')
@login_required
def detail_page():
    return render_template('detail.html')

@app.route('/logout')
def logout_page():
    logout_user()
    flash("You have been logged out!", category='info')
    return redirect(url_for("home_page"))
