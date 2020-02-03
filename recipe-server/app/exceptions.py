from marshmallow import ValidationError


def init_error_handlers(app):
    @app.errorhandler(ValidationError)
    def handle_error(e):
        return e.messages, 400
