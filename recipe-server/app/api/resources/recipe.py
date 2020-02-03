from flask import current_app as app
from flask import Blueprint, request, jsonify
from flask_restful import Api, Resource
from app.models import Recipe
from app.extensions import db
from app.serializers import RecipeSchema


recipe_bp = Blueprint('recipe', __name__)
recipe_api = Api(recipe_bp)


class RecipeResource(Resource):
    def get(self):
        """
        List recipes
        ---
        tags:
            - Recipe
        responses:
            200:
                description: successful operation
                schema:
                    type: array
                examples:
                    []
        """
        app.logger.info("This is test logging")
        recipes_schema = RecipeSchema(many=True)

        all_recipes = Recipe.query.all()
        return recipes_schema.jsonify(all_recipes)

    def post(self):
        """
        Add recipes
        ---
        tags:
            - Recipe
        parameters:
            - in: body
              name: body
              schema:
                type: object
                properties:
                    task:
                        type: string
                        default: My Task
        responses:
            201:
                description: successful operation
                schema:
                    type: object
                examples:
                    {
                        "name": "Pie",
                        "ingredients": "cream",
                        "difficulty": "easy",
                        "prep_time": "32",
                        "prep_guide": "cook pie"
                    }
        """

        recipe_schema = RecipeSchema()
        json_data = request.get_json()
        recipe = recipe_schema.load(json_data)
        app.logger.info(recipe)

        db.session.add(recipe)
        db.session.commit()

        return recipe_schema.jsonify(recipe)


recipe_api.add_resource(RecipeResource, '/recipes')
