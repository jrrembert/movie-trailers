#!/usr/bin/env python

class Movie(object):
    """
    Creates a Movie object.

    Required parameters:

    1. id (cannot be None)

    Optional parameters:

    1. title
    2. poster_image_url
    3. trailer_youtube_url
    4. synopsis
    5. critics_rating
    6. mpaa_rating
    7. year
    """
    
    def __init__(self, default=None, **kwargs):
        self.id = kwargs.get('id', default)
        self.title = kwargs.get('title', default)
        self.poster_image_url = kwargs.get('poster_image_url', default)
        self.trailer_youtube_url = kwargs.get('trailer_youtube_url', default)
        self.synopsis = kwargs.get('synopsis', default)
        self.critics_rating = kwargs.get('critics_rating', default)
        self.mpaa_rating = kwargs.get('mpaa_rating', default)
        self.year = kwargs.get('year', default)