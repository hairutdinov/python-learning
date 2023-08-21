from flask import Flask, render_template, redirect, url_for, request
from flask_bootstrap import Bootstrap5
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, FloatField, TextAreaField
from wtforms.validators import DataRequired, NumberRange
import requests
from kinopoisk_dev import KinopoiskDev, MovieParams, MovieField

KINOPOISK_ENDPOINT = 'https://api.kinopoisk.dev/v1.2/movie/search'
KINOPOISK_TOKEN = '0K7R08S-ZKJMQFV-K5G8E53-815JR1W'
SECRET_KEY = '6ImAKbmxphfq3tuYTwrJ44QsrzQ='
SQLALCHEMY_DATABASE_URI = 'sqlite:///movie-collection.db'

app = Flask(__name__)
app.config['SECRET_KEY'] = SECRET_KEY
Bootstrap5(app)

db = SQLAlchemy()
app.config['SQLALCHEMY_DATABASE_URI'] = SQLALCHEMY_DATABASE_URI
db.init_app(app)

kp = KinopoiskDev(token=KINOPOISK_TOKEN)


class Movie(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String, unique=True, nullable=False)
    year = db.Column(db.Integer, nullable=False)
    description = db.Column(db.String, nullable=False)
    rating = db.Column(db.Float)
    ranking = db.Column(db.Integer)
    review = db.Column(db.String)
    img_url = db.Column(db.String, nullable=False)


class RateMovieForm(FlaskForm):
    rating = FloatField(label='Your Rating Out of 10 e.g. 7.5', validators=[DataRequired(), NumberRange(min=0, max=10)])
    review = TextAreaField(label='Your Review', validators=[DataRequired()], render_kw={'rows': 5})
    done_btn = SubmitField(label='Done')


class AddMovieForm(FlaskForm):
    title = StringField(label='Movie Title', validators=[DataRequired()])
    add_movie_btn = SubmitField(label='Add Movie')


@app.route("/")
def home():
    movies = db.session.execute(
        db.select(Movie).order_by(Movie.rating)
    ).scalars()
    return render_template("index.html", movies=movies)


@app.route('/rate-movie', methods=['GET', 'POST'])
def rate_movie():
    movie_id = request.args['id']
    movie = db.get_or_404(Movie, movie_id)
    form = RateMovieForm(rating=movie.rating, review=movie.review)
    if form.validate_on_submit():
        movie.rating = form.rating.data
        movie.review = form.review.data
        db.session.commit()
        # return redirect(url_for('edit', id=movie.id))
        return redirect(url_for('home'))
    return render_template('edit.html', movie=movie, form=form)


@app.route('/delete')
def delete():
    movie_id = request.args['id']
    movie = db.get_or_404(Movie, movie_id)
    db.session.delete(movie)
    db.session.commit()
    return redirect(url_for('home'))


@app.route('/add', methods=['GET', 'POST'])
def add():
    form = AddMovieForm()
    if form.validate_on_submit():
        # response = requests.get(
        #     KINOPOISK_API_ENDPOINT,
        #     params={'query': form.title.data},
        #     headers={'X-API-KEY': KINOPOISK_TOKEN}
        # )
        # print(response.json())
        items = kp.find_many_movie(params=[
            MovieParams(keys=MovieField.NAME, value=form.title.data),
            MovieParams(keys=MovieField.PAGE, value="1"),
            MovieParams(keys=MovieField.LIMIT, value="10")
        ])
        return render_template('select.html', movies=items.docs)
    return render_template('add.html', form=form)


@app.route('/find-movie/<int:id>')
def find_movie(id):
    movie = kp.find_one_movie(id)
    new_movie = Movie(
        title=movie.name,
        year=movie.year,
        description=movie.description,
        img_url=movie.poster.url,
    )
    db.session.add(new_movie)
    db.session.commit()
    return redirect(url_for('rate_movie', id=new_movie.id))


with app.app_context():
    db.create_all()

# with app.app_context():
#     new_movie = Movie(
#         title="Phone Booth",
#         year=2002,
#         description="Publicist Stuart Shepard finds himself trapped in a phone booth, pinned down by an extortionist's sniper rifle. Unable to leave or receive outside help, Stuart's negotiation with the caller leads to a jaw-dropping climax.",
#         rating=7.3,
#         ranking=10,
#         review="My favourite character was the caller.",
#         img_url="https://image.tmdb.org/t/p/w500/tjrX2oWRCM3Tvarz38zlZM7Uc10.jpg"
#     )
#     db.session.add(new_movie)
#     db.session.commit()

if __name__ == '__main__':
    app.run(debug=True, port=8000)
