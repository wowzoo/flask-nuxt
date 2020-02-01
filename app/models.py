import enum

from app.extensions import db


class DifficultyEnum(enum.Enum):
    easy = 'Easy'
    medium = 'Medum'
    hard = 'Hard'


class Recipe(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(128))
    ingredients = db.Column(db.String(400))
    # picture = db.Column(db.String)
    difficulty = db.Column(
        db.Enum(DifficultyEnum),
        default=DifficultyEnum.easy,
        nullable=False
    )
    prep_time = db.Column(db.Integer)
    prep_guide = db.Column(db.Text)

    def __repr__(self):
        return "Recipe for {}".format(self.name)
