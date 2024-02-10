from flask import Flask, request, render_template, redirect
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import DataRequired
import shutil


class LoginForm(FlaskForm):
    IdAst = StringField('Id астронавта', validators=[DataRequired()])
    PassAst = PasswordField('Пароль астронавта', validators=[DataRequired()])
    IdCom = StringField('Id капитана', validators=[DataRequired()])
    PassCom = PasswordField('Пароль капитана', validators=[DataRequired()])
    remember_me = BooleanField('Запомнить меня')
    submit = SubmitField('Войти')


app = Flask(__name__)


@app.route('/')
@app.route('/index')
def index():
    user = "Заготова"
    return render_template('index.html', title=user)


@app.route('/answer')
@app.route('/auto_answer')
def answer(title='Заголовка',
           surname='Watny',
           name='Mark',
           education='выше среднего',
           profession='штурман марсохода',
           sex='male',
           motivation='Всегда мечтал застрять на Марсе!',
           ready='True'):
    return render_template('auto_answer.html', title=title,
                           surname=surname,
                           name=name,
                           education=education,
                           profession=profession,
                           sex=sex,
                           motivation=motivation,
                           ready=ready)


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        return redirect('/success')
    return render_template('login.html', title='Авторизация', form=form)


@app.route('/distribution')
def distribution():
    return render_template('distribution.html')


@app.route('/table/<male>/<female>')
def table(male, female):
    if male == 'male':
        p = 1
    else:
        p = 2

    try:
        if int(female) <= 15:
            n = 1
            p = p * 10 + 1
        else:
            n = 2
            p = p * 10 + 2
        return render_template('table.html', pol=p, age=n)
    except Exception:
        pass


@app.route('/galery', methods=['POST', 'GET'])
def galery():
    if request.method == 'POST':
        shutil.copyfile(request.form['file'], '/static/img/mars1.png')
    return render_template('galery.html')


if __name__ == '__main__':
    app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'
    app.run(port=8000, host='127.0.0.1')
