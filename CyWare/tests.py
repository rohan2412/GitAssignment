from django.test import TestCase
from utils import get_search_url


class TestGetSearchUrl(TestCase):

    def setUp(self):
        self.url = 'https://www.github.com/search/users'
        self.search_params = {
            'q': 'rohan',
        }

    def test_positive_1(self):
        exp = 'https://www.github.com/search/users?q=rohan'
        actual = get_search_url(url=self.url, search_params=self.search_params)
        self.assertEqual(exp, actual)

    def test_positive_2(self):
        self.url = 'https://www.github.com/search/users/'
        exp = 'https://www.github.com/search/users/?q=rohan'
        actual = get_search_url(url=self.url, search_params=self.search_params)
        self.assertEqual(exp, actual)

    def test_positive_3(self):
        self.url = 'https://www.github.com/search/users?page=1'
        exp = 'https://www.github.com/search/users?page=1&q=rohan'
        actual = get_search_url(url=self.url, search_params=self.search_params)
        self.assertEqual(exp, actual)

    def test_positive_4(self):
        self.search_params = {}
        exp = 'https://www.github.com/search/users'
        actual = get_search_url(url=self.url, search_params=self.search_params)
        self.assertEqual(exp, actual)

