from flask import Flask, render_template, redirect, url_for
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectField
from wtforms.validators import DataRequired, URL
from flask_bootstrap import Bootstrap5
import csv

app = Flask(__name__)
bootstrap = Bootstrap5(app)

app.secret_key = 'lBE3f67u4W3L29+pLXGhu1bFuuk='


class CafeForm(FlaskForm):
    cafe_name = StringField(label='Cafe Name', validators=[DataRequired()])
    location = StringField(label='Cafe Location on Google Maps (URL)', validators=[DataRequired(), URL()])
    open = StringField(label='Opening Time e.g. 8AM', validators=[DataRequired()])
    close = StringField(label='Closing Time e.g. 5:30PM', validators=[DataRequired()])
    coffee_rating = SelectField(
        label='Coffee Rating',
        choices=['✘', '☕️', '☕️☕️', '☕️☕️☕️', '☕️☕️☕️☕️', '☕️☕️☕️☕️☕️'],
        validators=[DataRequired()]
    )
    witi_strength = SelectField(
        label='Wii Strength Rating',
        choices=['✘', '💪', '💪💪', '💪💪💪', '💪💪💪💪', '💪💪💪💪💪'],
        validators=[DataRequired()]
    )
    power = SelectField(
        label='Power Socket Availability',
        choices=['✘', '🔌', '🔌🔌', '🔌🔌🔌', '🔌🔌🔌🔌', '🔌🔌🔌🔌🔌'],
        validators=[DataRequired()]
    )
    submit = SubmitField(label='Submit')


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/cafes')
def cafes():
    cafes = []
    with open('cafe-data.csv', 'r', newline='') as file:
        reader = csv.reader(file)
        for row in reader:
            cafes.append(row)
    return render_template('cafes.html', cafes=cafes)


@app.route('/add', methods=['GET', 'POST'])
def add():
    cafe_form = CafeForm()
    if cafe_form.validate_on_submit():
        with open('cafe-data.csv', 'a', newline='') as file:
            row = [
                cafe_form.cafe_name.data,
                cafe_form.location.data,
                cafe_form.open.data,
                cafe_form.close.data,
                cafe_form.coffee_rating.data,
                cafe_form.witi_strength.data,
                cafe_form.power.data,
            ]
            file.write('\n' + ','.join(row))
            return redirect(url_for('cafes'))

    return render_template('add.html', form=cafe_form)


if __name__ == '__main__':
    app.run(debug=True, port=8000)
