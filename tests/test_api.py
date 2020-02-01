import json


def test_recipe_post(client):
    rv = client.post('/api/recipes')
    assert json.loads(rv.data.decode("utf-8")) == 'test'


def test_recipe_get(client):
    rv = client.get('/api/recipes')
    recipe_list = json.loads(rv.data.decode('utf-8'))

    assert len(recipe_list) == 1
