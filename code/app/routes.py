from flask_restplus import Resource, Api
from app import app
from flask import jsonify, Blueprint, request
from app import GetInfo


blueprint = Blueprint('api', __name__)
api = Api(blueprint,
          default='',
          title='Github Repositories',
          version='1.0',
          description='Get information about users repositories on Github',
          doc='/api/documentation',
          default_label='Options')


@app.route("/")
def home():
    url = f'http://{request.headers.get("Host")}'
    result = {'all_informations': f'{url}/{{user}}',
              'repositories': f'{url}/{{user}}/repos',
              'sum_of_stars': f'{url}/{{user}}/stars',
              'documentation': f'{url}/api/documentation'}
    return result


app.register_blueprint(blueprint)


@api.route('/<name>')
@api.response(200, 'Success')
@api.response(401, 'Unauthorized')
@api.response(403, 'Forbidden')
@api.response(404, 'User not found.')
@api.response(408, 'Request timeout')
class UserInformations(Resource):
    def get(self, name):
        return jsonify(GetInfo(name).get_data().return_user_info())


@api.route("/<name>/repos")
@api.response(200, 'Success')
@api.response(401, 'Unauthorized')
@api.response(403, 'Forbidden')
@api.response(404, 'User not found.')
@api.response(408, 'Request timeout')
class UserRepositories(Resource):
    def get(self, name):
        return jsonify(GetInfo(name).get_data().return_repos())


@api.route("/<name>/stars")
@api.response(200, 'Success')
@api.response(401, 'Unauthorized')
@api.response(403, 'Forbidden')
@api.response(404, 'User not found.')
@api.response(408, 'Request timeout')
class UserStars(Resource):
    def get(self, name):
        return jsonify(GetInfo(name).get_data().return_stars())
