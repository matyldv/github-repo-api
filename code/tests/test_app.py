import requests
import unittest

URL = 'http://127.0.0.1:5000'


class TestApp(unittest.TestCase):

    def test_app_request(self):
        user_login = 'matyldv'
        response = requests.get(f'{URL}/{user_login}')

        self.assertTrue(response.ok)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json().get('login'), user_login)

    def test_wrong_user(self):
        response = requests.get(f'{URL}/matylvd')

        self.assertFalse(response.ok)
        self.assertEqual(response.status_code, 404)
        self.assertEqual(response.json().get('error'), 'not_found')

    def test_wrong_page(self):
        response = requests.get(f'{URL}/matyldv/repoo')

        self.assertFalse(response.ok)
        self.assertEqual(response.status_code, 404)
        self.assertEqual(response.json().get('error'), 'not_found')

    def test_get_stars(self):
        stars_count = {"all_stars": 3}
        response = requests.get(f'{URL}/roztropny/stars')

        self.assertDictEqual(response.json(), stars_count)

    def test_get_repos(self):
        repo_name = {
                    "name": "concurrency_learning",
                    "stars": 1
        }
        response = requests.get(f'{URL}/roztropny/repos')

        self.assertIn(repo_name, response.json())


if __name__ == '__main__':
    unittest.main()
