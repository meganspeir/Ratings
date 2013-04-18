from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine, ForeignKey
from sqlalchemy import Column, Integer, String, DateTime, Date

from sqlalchemy.orm import sessionmaker, scoped_session, relationship, backref
import os
import correlation

db_uri = os.environ.get("Database_URL", "sqlite:///ratings.db")

engine = create_engine("sqlite:///ratings.db", echo=False)
session = scoped_session(sessionmaker(bind=engine,
                                      autocommit = False,
                                      autoflush = False))

Base = declarative_base()
Base.query = session.query_property()

### Class declarations go here

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key = True)
    email = Column(String(64), nullable=True)
    password = Column(String(64), nullable=True)
    age = Column(Integer, nullable=True)
    zipcode = Column(String(15), nullable=True)

    def __init__(self, email =None, password =None, age=None, zipcode=None):
        self.email = email
        self.password = password
        self.age = age
        self.zipcode = zipcode

    def similarity(self, other):
        u_ratings = {}
        paired_ratings = []
        for r in self.ratings:
            u_ratings[r.movie_id] = r

        for r in other.ratings:
            u_r = u_ratings.get(r.movie_id)
            if u_r:
                paired_ratings.append( (u_r.rating, r.rating) )

        if paired_ratings:
            return correlation.pearson(paired_ratings)
        else:
            return 0.0

    def predict_rating(self, movie):
        if not self.ratings: return None
        ratings = self.ratings
        other_ratings=movie.ratings
        similarities = [ (self.similarity(r.user), r) \
            for r in other_ratings ]
        similarities.sort(reverse = True)
        top = similarities[0]

        similarities = [ sim for sim in similarities if sim[0] > 0 ]
        if not similarities:
            return None
        prediction = sum([ sim * r.rating for sim, r in similarities ])
        denominator = sum( sim[0] for sim in similarities )
        prediction = float(prediction)/denominator
        return prediction

class Movie(Base):
    __tablename__ = "movies"

    id = Column(Integer, primary_key = True)
    title = Column(String(100))

    def __init__(self, title):
        self.title = title

class Rating(Base):
    __tablename__ = "ratings"

    id = Column(Integer, primary_key = True)
    rating = Column(Integer)
    user_id = Column(Integer, ForeignKey('users.id'))
    movie_id = Column(Integer, ForeignKey('movies.id'))

    user = relationship("User",
            backref=backref("ratings", order_by=id))

    def __init__(self, rating, user_id, movie_id):
        self.rating = rating
        self.user_id = user_id
        self.movie_id = movie_id


### End class declarations

def create_db():
    Base.metadata.create_all(engine)

def connect():
    global ENGINE
    global Session

    ENGINE = create_engine("sqlite:///ratings.db", echo=True)
    Session = sessionmaker(bind=ENGINE)

    return Session()

def main():
    """In case we need this for something"""
    pass

if __name__ == "__main__":
    main()
