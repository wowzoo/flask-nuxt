import json

from flask import Flask, jsonify


class APIException(Exception):
    def __init__(self, message=''):
        self.message = message


def init_error_handlers(app: Flask):
    @app.errorhandler(APIException)
    def handle_error(error) -> (json, int):
        response = {
            'error': {
                'type': error.__class__.__name__,
                'message': error.message
            }
        }

        return jsonify(response), error.status_code
