import json


def test_recipe_post(client):
    mimetype = 'application/json'
    headers = {
        'Content-Type': mimetype,
        'Accept': mimetype
    }
    data = {
        "name": "Meat Pie",
        "ingredients": "meat",
        "difficulty": "medium",
        "prep_time": 60,
        "prep_guide": "cook meat pie"
    }
    url = '/api/recipes'

    response = client.post(url, data=json.dumps(data), headers=headers)

    assert response.content_type == mimetype

    assert json.loads(response.data.decode('utf-8')) == data


def test_recipe_get(client):
    response = client.get('/api/recipes')
    recipe_list = json.loads(response.data.decode('utf-8'))

    assert len(recipe_list) == 2
