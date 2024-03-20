from flask_migrate import Migrate, upgrade as upgrade_schema
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()
migrate = Migrate()


def init_app(app):
    db.init_app(app)
    migrate.init_app(app, db)
    with app.app_context():
        upgrade_schema()
