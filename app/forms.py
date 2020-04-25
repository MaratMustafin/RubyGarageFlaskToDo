from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import DataRequired,EqualTo
from app.models import Users

class LoginForm(FlaskForm):
    username = StringField('Логин', validators=[DataRequired('Введенные данные не верны')])
    password = PasswordField('Пароль', validators=[DataRequired('Введенные данные не верны')])
    remember_me = BooleanField('Запомнить меня')
    submit = SubmitField('Войти')

class RegistrationForm(FlaskForm):
    username = StringField('Логин', validators=[DataRequired('Введенные данные не верны')])
    password = PasswordField('Пароль', validators=[DataRequired('Введенные данные не верны')])
    password2 = PasswordField(
        'Повторить пароль', validators=[DataRequired('Введенные данные не верны'), EqualTo('password',message='Пароли не совпадают')])
    submit = SubmitField('Зарегистрироваться')

    def validate_username(self, username):
        user = Users.query.filter_by(username=username.data).first()
        if user is not None:
            raise ValidationError('Логин занят')
