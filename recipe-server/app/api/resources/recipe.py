from flask import current_app as app
from flask import Blueprint, request, jsonify
from flask_restful import Api, Resource
from app.models import Recipe
from app.extensions import db
from app.serializers import RecipeSchema


recipe_bp = Blueprint('recipe', __name__)
recipe_api = Api(recipe_bp)


class RecipeListResource(Resource):
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
        # app.logger.info("This is test logging")
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
        json_data = dict(request.form)
        recipe = recipe_schema.load(json_data)

        db.session.add(recipe)
        db.session.commit()

        return recipe_schema.jsonify(recipe)


class RecipeResource(Resource):
    recipe_schema = RecipeSchema()

    def get(self, recipe_id):
        recipe_to_return = Recipe.query.get(recipe_id)
        return self.recipe_schema.jsonify(recipe_to_return)

    def patch(self, recipe_id):
        json_data = dict(request.form)
        recipe_to_update = Recipe.query.filter_by(id=recipe_id).update(json_data)
        db.session.commit()

        return self.recipe_schema.jsonify(recipe_to_update)

    def delete(self, recipe_id):
        recipe_to_delete = Recipe.query.get(recipe_id)
        db.session.delete(recipe_to_delete)
        db.session.commit()

        return self.recipe_schema.jsonify(recipe_to_delete)


recipe_api.add_resource(RecipeListResource, '/recipes')
recipe_api.add_resource(RecipeResource, '/recipes/<int:recipe_id>')
