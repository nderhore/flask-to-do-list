from flask import Flask


from src.api.api import api_bp
from src.api.task import tasks_bp
from src.config.config import Config
from src.config.database import db


def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    # Initialisez db avec l'application
    db.init_app(app)

    # Importez les modèles et créez les tables
    with app.app_context():
        from src.model.Task import Task
        db.create_all()

    # Importez et enregistrez les blueprints
    from src.api.api import api_bp
    from src.api.task import tasks_bp
    app.register_blueprint(tasks_bp, url_prefix="/tasks")
    app.register_blueprint(api_bp, url_prefix="/api")
    return app


if __name__ == "__main__":
    app = create_app()
    app.run(debug=True)
