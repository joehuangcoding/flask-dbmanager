from flask import Flask

def create_app():
    """Create and configure an instance of the Flask application."""
    app = Flask(__name__)
    # app.config.from_pyfile("config.py", silent=True)
    app.config.from_mapping(
        DB_USER="root",
        DB_PASS="root",
        DB_HOST="localhost",
        DB_PORT="3306",
        DB_NAME="blog"
    )
    import dbmanager
    app.register_blueprint(dbmanager.bp)
    app.add_url_rule("/", endpoint="index")
    return app
