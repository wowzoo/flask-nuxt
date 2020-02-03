from flask import Flask


def init_app(app: Flask):
    from .resources.recipe import recipe_bp
    app.register_blueprint(recipe_bp, url_prefix='/api')
