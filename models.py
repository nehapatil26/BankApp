from Bank import bcrypt
from flask_login import UserMixin
from Bank import db, login_manager


@login_manager.user_loader
def load_user(cust_id):
    return Customer.query.get(int(cust_id))

class Customer(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(length=30), nullable=False)
    last_name = db.Column(db.String(length=50), nullable=False)
    mobileNumber = db.Column(db.String(length=10), nullable=False, unique=True)
    address = db.Column(db.String(length=200), nullable=False)
    city = db.Column(db.String(length=50), nullable=False)
    state = db.Column(db.String(length=50), nullable=False)
    password_hash = db.Column(db.String(length=60), nullable=False)
    zip_code = db.Column(db.Integer(), nullable=False)
    accounts = db.relationship('Account', backref='owned_user', lazy=True)

    @property
    def password(self):
        return self.password

    @password.setter
    def password(self, plain_text_password):
        self.password_hash = bcrypt.generate_password_hash(plain_text_password).decode('utf-8')

    def check_password_correction(self, attempted_password):
        return bcrypt.check_password_hash(self.password_hash, attempted_password)


class Account(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    balance = db.Column(db.String(length=20), nullable=False, default=0)
    acc_no = db.Column(db.Integer, db.ForeignKey('customer.id'), nullable=False)
