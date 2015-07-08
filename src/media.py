#!/usr/bin/env python

class Movie(object):
    """
    Creates a Movie object:

    Valid parameters are:

    title
    poster_image_url
    trailer_youtube_url
    """
    
    def __init__(self, default=None, **kwargs):
        

        self.title = kwargs.get('title', default)
        self.poster_image_url = kwargs.get('poster_image_url', default)
        self.trailer_youtube_url = kwargs.get('trailer_youtube_url', default)