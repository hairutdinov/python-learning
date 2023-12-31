from flask import Flask, render_template, redirect
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, EmailField
from wtforms.validators import DataRequired, Length, Email
from flask_bootstrap import Bootstrap5

'''
Red underlines? Install the required packages first: 
Open the Terminal in PyCharm (bottom left). 

On Windows type:
python -m pip install -r requirements.txt

On MacOS type:
pip3 install -r requirements.txt

This will install the packages from requirements.txt for this project.
'''


class LoginForm(FlaskForm):
    email = EmailField(label='Email', validators=[DataRequired(), Email()])
    password = PasswordField(label='Password', validators=[DataRequired(), Length(min=8)])
    submit = SubmitField(label='Log in')


app = Flask(__name__)

bootstrap = Bootstrap5(app)

SECRET_KEY = 'aVDVg/5UOIBHF+pXFXoZReeLKQ8='
WTF_CSRF_SECRET_KEY = 'G2r74+PlkFnL3h11m0c36C1uyjE='
# app.config['SECRET_KEY'] = SECRET_KEY
app.secret_key = SECRET_KEY
app.config['WTF_CSRF_SECRET_KEY'] = WTF_CSRF_SECRET_KEY


@app.route("/")
def home():
    return render_template('index.html')


@app.route('/login', methods=['POST', 'GET'])
def login():
    login_form = LoginForm()
    if login_form.validate_on_submit():
        if login_form.email.data == 'admin@email.com' and login_form.password.data == '12345678':
            return render_template('success.html')
        else:
            return render_template('denied.html')
    return render_template('login.html', form=login_form)

if __name__ == '__main__':
    app.run(debug=True)
