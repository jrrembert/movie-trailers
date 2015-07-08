import unittest

from media import Movie


class TestEntertainmentCenter(unittest.TestCase):
    
    def setUp(self):
        movie_one = Movie(title="Superman Lives")
        movie_two = Movie(title="Batman Dies")
        self.movie_list = [movie_one, movie_two]
        
    def test_create_movie_list(self):
        self.assertEqual(len(self.movie_list), 2)

if __name__ == '__main__':
    unittest.main()