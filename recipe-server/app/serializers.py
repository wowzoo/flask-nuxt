from app.models import Recipe, DifficultyEnum
from app.extensions import ma
from marshmallow import ValidationError


def validate_difficulty(value):
    if value not in DifficultyEnum._member_names_:
        raise ValidationError("Value must be one of enum name")


class RecipeSchema(ma.ModelSchema):
    difficulty = ma.String(validate=validate_difficulty)

    class Meta:
        model = Recipe
        # Fields to expose
        fields = ('name', 'ingredients', 'difficulty', 'prep_time', 'prep_guide')
