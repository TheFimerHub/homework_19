from dao.directors_dao import DirectorDao
from dao.genres_dao import GenreDao
from dao.movies_dao import MovieDao
from dao.users_dao import UserDao
from service.auth_serv import AuthService
from service.directors_serv import DirectorServise
from service.genres_serv import GenreServise
from service.movies_serv import MovieServise
from service.users_serv import UserService
from setup_db import db

movie_dao = MovieDao(db.session)
movie_service = MovieServise(dao=movie_dao)

genre_dao = GenreDao(db.session)
genre_service = GenreServise(dao=genre_dao)

director_dao = DirectorDao(db.session)
director_service = DirectorServise(dao=director_dao)

user_dao = UserDao(db.session)
user_service = UserService(dao=user_dao)

auth_service = AuthService(user_service)