import unittest

from media import Movie


class TestMovie(unittest.TestCase):
    
    def setUp(self):
        self.movie = Movie()
        
    def test_create_empty_movie(self):
        self.assertEqual(self.movie.title, None)

    def test_create_new_movie(self):
        new_movie = Movie(title='Superman Lives')
        self.assertEqual(new_movie.title, "Superman Lives")

if __name__ == '__main__':
    unittest.main()