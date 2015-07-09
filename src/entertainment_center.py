#!/usr/bin/env python
import json
import os

from media import Movie
from fresh_tomatoes import create_movie_tiles_content, open_movies_page


movie_data_path = os.path.join(
    os.path.dirname(__file__),'../data/movies.json')
with open(movie_data_path, 'r') as f:
    movie_data = json.load(f)

movie_list = []

for index in range(0, len(movie_data)):
    new_movie = Movie(**movie_data[index])
    movie_list.append(new_movie)

if __name__ == '__main__':
    open_movies_page(movie_list)


