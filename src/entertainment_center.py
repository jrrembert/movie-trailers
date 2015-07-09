#!/usr/bin/env python
import json
import os

from media import Movie
from fresh_tomatoes import create_movie_tiles_content, open_movies_page


class EntertainmentCenter():
    """
    Loads movie data and builds a list of Movie objects.
    """
    def __init__(self):
        self.movie_data_path = os.path.join(
            os.path.dirname(__file__),
            '../data/movies.json')

    def load_data(self, data_path):
        """
        Read movie data from file and convert to json.
        """
        with open(data_path, 'r') as f:
            movie_data = json.load(f)
            return movie_data

    def create_movie_list(self, movie_data):        
        """
        Build a list of movies based on a json-formatted array of movies.
        """
        self.movie_list = []

        for index in range(0, len(movie_data)):
            new_movie = Movie(**movie_data[index])
            self.movie_list.append(new_movie)
            
        return self.movie_list

if __name__ == '__main__':
    movies = EntertainmentCenter()
    movie_data = movies.load_data(movies.movie_data_path)
    movie_list = movies.create_movie_list(movie_data)

    # Build HTML and open page
    open_movies_page(movie_list)


