# -*- coding: utf-8 -*-
from flask import render_template, flash, redirect, url_for, request
from flask_login import login_user, logout_user, current_user, login_required
from app import app,db
from app.forms import LoginForm,RegistrationForm
from app.models import Users,Projects,Tasks


@app.route('/')
@app.route('/index')
def index():
    proj = Projects.query.filter_by(user_id='guest').all()
    task = Tasks.query.order_by(Tasks.task_position).all()
    if current_user.is_authenticated:
        proj = Projects.query.filter_by(user_id=current_user.id).all()
    return render_template('index.html',title='Welcome',proj=proj,task=task)

@app.route('/mytask')
@login_required
def mytask():
    return render_template('mytask.html',title='ToDo')

@app.route('/login',methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = LoginForm()
    if form.validate_on_submit():
        user = Users.query.filter_by(username=form.username.data).first()
        if user is None or not user.check_password(form.password.data):
            flash('Неверное имя пользователя или пароль')	
            return redirect(url_for('login'))
        login_user(user,remember=form.remember_me.data)
        return redirect(url_for('mytask'))
    return render_template('login.html', title='Логин', form=form)
    
@app.route('/register', methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('mytask'))
    form = RegistrationForm()
    if form.validate_on_submit():
        user = Users(username=form.username.data)
        user.set_password(form.password.data)
        db.session.add(user)
        db.session.commit()
        flash('Поздравляю теперь вы зарегистрированы! Войдите в систему')
        return redirect(url_for('login'))
    return render_template('register.html', title='Регистрация', form=form)


@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('index'))	

from .main import main as main_blueprint
app.register_blueprint(main_blueprint)