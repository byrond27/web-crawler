import unittest
import requests


class MyTestCase(unittest.TestCase):
    URL = 'https://news.ycombinator.com/'

    def test_should_status_code_200(self):
        page = requests.get(self.URL)
        self.assertEqual(page.status_code, 200)


if __name__ == '__main__':
    unittest.main()
