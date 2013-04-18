import model
import csv

def load_users(session):
    # use u.user
    with open('seed_data/u.user', 'rb') as f:
        reader = csv.reader(f, delimiter='|')
        for row in reader:
            age = row[1]
            print age
            zipcode = row[4]
            user = model.User(age=age, zipcode=zipcode)
            session.add(user)
            session.commit()

def load_movies(session):
    # use u.item
    with open('seed_data/u.item', 'rb') as f:
        reader = csv.reader(f, delimiter='|')
        for row in reader:
            title = row[1]
            title = title.decode('latin-1')
            movie = model.Movie(title)
            session.add(movie)
            session.commit()

def load_ratings(session):
    # use u.data
    with open('seed_data/u.data', 'rb') as f:
        reader = csv.reader(f, delimiter=' ')
        for row in reader:
            items = row[0].split()
            user_id = items[0]
            movie_id = items[1]
            rating_val = items[2]

            rating = model.Rating(rating_val, user_id, movie_id)
            session.add(rating)
        session.commit()

def main(session):
    # You'll call each of the load_* functions with the session as an argument
    load_users(session)
    load_movies(session)
    load_ratings(session)

if __name__ == "__main__":
    s = model.connect()
    main(s)
