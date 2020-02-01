from flask import current_app as app
from flask import Blueprint
from flask_restful import Api, Resource

from app.models import Recipe


recipe_bp = Blueprint('recipe', __name__)
recipe_api = Api(recipe_bp)


class RecipeResource(Resource):
    def get(self):
        app.logger.info("This is test logging")
        query = Recipe.query.all()
        data = []
        for item in query:
            data.append({
                'id': item.id,
                'name': item.name
            })

        return data

    def post(self):
        return 'test'


recipe_api.add_resource(RecipeResource, '/recipes')
