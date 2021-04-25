from flask import jsonify


class Server:
    def __init__(self, app):
        self.app = app

    def config(self):
        self.app.config['JSONIFY_PRETTYPRINT_REGULAR'] = True
        self.app.config['JSON_SORT_KEYS'] = False
        self.app.config["PROPAGATE_EXCEPTIONS"] = False
        self.app.config.SWAGGER_UI_DOC_EXPANSION = 'list'
        self.app.config['ERROR_404_HELP'] = False

    def run(self):
        @self.app.errorhandler(400)
        def bad_request(err):
            return jsonify({'error': 'bad_request', 'error_msg': 'Bad request'}), err.code

        @self.app.errorhandler(401)
        def unauthorized(err):
            return jsonify({'error': 'unauthorized', 'error_msg': 'Unauthorized, Github token is invalid'}), err.code

        @self.app.errorhandler(403)
        def forbidden(err):
            return jsonify({'error': 'forbidden', 'error_msg': 'Forbidden, try to set a Github token'}), err.code

        @self.app.errorhandler(404)
        def page_not_found(err):
            return jsonify({'error': 'not_found', 'error_msg': 'Not found'}), err.code

        @self.app.errorhandler(405)
        def method_not_allowed(err):
            return jsonify({'error': 'method_not_allowed', 'error_msg': 'Method not allowed'}), err.code

        @self.app.errorhandler(408)
        def request_timeout(err):
            return jsonify({'error': 'request_timeout', 'error_msg': 'Request timeout'}), err.code

        @self.app.errorhandler(500)
        def internal_server_error(err):
            return jsonify({'error': 'internal_server_error', 'error_msg': 'Internal server error'}), err.code

        @self.app.errorhandler(Exception)
        def handle_error(err):
            return jsonify({'error': 'unexpected_error', 'error_msg': 'Unexpected error'})
