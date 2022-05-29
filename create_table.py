from config import Config
from app import create_app
from setup_db import db

app = create_app(Config)

with app.app_context():
    db.drop_all()
    db.create_all()
