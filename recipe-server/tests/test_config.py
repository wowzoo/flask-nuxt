from app import create_app


def test_config_development():
    app = create_app(config_name='development')

    assert "SECRET_KEY" in app.config

    assert app.config['DEBUG'] == True
    assert app.config['TESTING'] == False


def test_config_production():
    app = create_app(config_name='production')

    assert "SECRET_KEY" in app.config

    assert app.config['DEBUG'] == False
    assert app.config['TESTING'] == False
    assert app.config['PROPAGATE_EXCEPTIONS'] == True
