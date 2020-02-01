from app import create_app
from config.config import DEVELOPMENT_STAGE

app = create_app(config_name=DEVELOPMENT_STAGE)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8000, debug=True)
