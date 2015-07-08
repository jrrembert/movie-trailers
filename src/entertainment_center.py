#!/usr/bin/env python
from media import Movie
from fresh_tomatoes import create_movie_tiles_content, open_movies_page


movies = [
    {
    'title': 'Superman Lives',
    'poster_image_url': 'http://resizing.flixster.com/4wO5bBcgO15zfM7neVyjevhlQZc=/170x270/dkpu1ddg7pbsk.cloudfront.net/movie/11/19/12/11191223_ori.jpg',
    'trailer_youtube_url': 'https://www.youtube.com/watch?v=7TYJyCCO8Dc&t=19'
    },
    {
    'title': 'Batman Dies',
    'poster_image_url': 'http://resizing.flixster.com/4wO5bBcgO15zfM7neVyjevhlQZc=/170x270/dkpu1ddg7pbsk.cloudfront.net/movie/11/19/12/11191223_ori.jpg',
    'trailer_youtube_url': 'https://www.youtube.com/watch?v=7TYJyCCO8Dc&t=19'
    },
    {
    'title': 'Aquaman Swims',
    'poster_image_url': 'http://resizing.flixster.com/4wO5bBcgO15zfM7neVyjevhlQZc=/170x270/dkpu1ddg7pbsk.cloudfront.net/movie/11/19/12/11191223_ori.jpg',
    'trailer_youtube_url': 'https://www.youtube.com/watch?v=7TYJyCCO8Dc&t=19'
    },
    {
    'title': 'Wonder Woman Wonders',
    'poster_image_url': 'http://resizing.flixster.com/4wO5bBcgO15zfM7neVyjevhlQZc=/170x270/dkpu1ddg7pbsk.cloudfront.net/movie/11/19/12/11191223_ori.jpg',
    'trailer_youtube_url': 'https://www.youtube.com/watch?v=7TYJyCCO8Dc&t=19'
    }, 
    {
    'title': 'The Flash Flashes',
    'poster_image_url': 'http://resizing.flixster.com/4wO5bBcgO15zfM7neVyjevhlQZc=/170x270/dkpu1ddg7pbsk.cloudfront.net/movie/11/19/12/11191223_ori.jpg',
    'trailer_youtube_url': 'https://www.youtube.com/watch?v=7TYJyCCO8Dc&t=19'
    }
]

movie_list = []

for index in range(0, len(movies)):
    new_movie = Movie(**movies[index])
    movie_list.append(new_movie)



if __name__ == '__main__':
    open_movies_page(movie_list)


