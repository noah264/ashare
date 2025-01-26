import os

from app import app

if __name__ == '__main__':
    app.run(host=os.getenv("FLASK_HOST", "0.0.0.0"), port=os.getenv("FLASK_PORT", "5000"), debug=os.getenv("FLASK_DEBUG", "true"))
