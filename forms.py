from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import Length, EqualTo, DataRequired, ValidationError
from Bank.models import Customer

class RegisterForm(FlaskForm):

    first_name = StringField(label='First Name:', validators=[Length(min=2, max=20), DataRequired()])
    last_name = StringField(label='Last Name:', validators=[Length(min=2, max=20), DataRequired()])
    mobileNumber = StringField(label='Mobile Number:', validators=[Length(min=10, max=10), DataRequired(message="Verify mobile number")])
    address = StringField(label='Address:', validators=[Length(max=100), DataRequired()])
    city = StringField(label='City:', validators=[Length(max=20), DataRequired()])
    state = StringField(label='State:', validators=[Length(max=20), DataRequired()])
    zip_code = StringField(label='Zipcode:', validators=[Length(max=10), DataRequired()])
    password1 = PasswordField(label='Enter Password:', validators=[Length(min=6), DataRequired()])
    password2 = PasswordField(label='Confirm Password:', validators=[EqualTo('password1'), DataRequired()])
    submit = SubmitField(label='Submit')

    def validate_mobileNumber(self, customer_to_check):
        mobileNumber = Customer.query.filter_by(mobileNumber=customer_to_check.data).first()
        if mobileNumber:
            raise ValidationError('Customer already exist!')

class LoginForm(FlaskForm):
    mobileNumber = StringField(label="Mobile Number:", validators=[DataRequired()])
    password = PasswordField(label="Password:", validators=[DataRequired()])
    submit = SubmitField(label='Login')

