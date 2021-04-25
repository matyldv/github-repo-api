import requests
import app
from flask import abort, jsonify
import os


class GetInfo:
    def __init__(self, name):
        self.name = name
        self.token = ''
        self.page = 1

    def get_token(self):
        try:
            self.token = os.getenv('APP_GITHUB_TOKEN')
            if self.token == '':
                raise Exception
            authorization = True
        except (OSError, Exception) as e:
            authorization = False
        return authorization

    def get_data(self):
        user = app.UserInfo(self.name)
        authorization = self.get_token()

        while True:
            try:
                if authorization:
                    r = requests.get(
                        f'https://api.github.com/users/{self.name}/repos?page={self.page}&per_page=100&type=all',
                        headers={'Authorization': f'Token {self.token}'})
                    r.raise_for_status()
                else:
                    r = requests.get(
                        f'https://api.github.com/users/{self.name}/repos?page={self.page}&per_page=100&type=all')
                    r.raise_for_status()
            except requests.exceptions.HTTPError as err:
                if err.response.status_code == 400:
                    abort(400, jsonify({'error': 'bad_request', 'error_msg': 'Bad request'}))
                elif err.response.status_code == 401:
                    abort(401, jsonify({'error': 'unauthorized', 'error_msg': 'Unauthorized, Github token is invalid'}))
                elif err.response.status_code == 403:
                    abort(403, jsonify({'error': 'forbidden', 'error_msg': 'Forbidden, try to set a Github token'}))
                elif err.response.status_code == 404:
                    abort(404, jsonify({'error': 'not_found', 'error_msg': 'Not found'}))
                elif err.response.status_code == 405:
                    abort(405, jsonify({'error': 'method_not_allowed', 'error_msg': 'Method not allowed'}))
                elif err.response.status_code == 408:
                    abort(408, jsonify({'error': 'request_timeout', 'error_msg': 'Request timeout'}))
                elif err.response.status_code == 500:
                    abort(500, jsonify({'error': 'internal_server_error', 'error_msg': 'Internal server error'}))
                else:
                    abort(err.response.status_code)
            else:
                if r.json():
                    for repo in r.json():
                        user.repositories.append({'name': repo.get('name'), 'stars': repo.get('stargazers_count')})
                else:
                    break
                self.page += 1
        return user
