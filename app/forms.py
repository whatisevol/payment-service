from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, \
    SubmitField, SelectField, TextAreaField, validators, FloatField
from wtforms.validators import DataRequired


class NameForm(FlaskForm):
    amount = FloatField('Payment amount', validators=[DataRequired()])
    currency = SelectField(u'Currency ', choices=[('EUR', 'EUR'), ('USD', 'USD'), ('RUB', 'RUB')])
    description = TextAreaField(u'Product description ', [validators.optional(), validators.length(max=200)])
    submit = SubmitField('Submit')
