from flask import Flask
from flask_login import LoginManager
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from sqlalchemy import text
from flask_bootstrap import Bootstrap
from flask_mail import Mail

db = SQLAlchemy()
migrate = Migrate()
login_manager = LoginManager()
mail = Mail()

def format_currency(value):
    """Format a number as currency."""
    return "${:,.2f}".format(value)

def create_app(settings_module):
    app = Flask(__name__)
    bootstrap = Bootstrap(app)
    app.config.from_object(settings_module)

    db.init_app(app)
    migrate.init_app(app, db)
    login_manager.init_app(app)
    mail.init_app(app)  # Inicializar Flask-Mail
    login_manager.login_view = "signin"

    # Configurar las credenciales de correo electrónico
    app.config.update(
        MAIL_SERVER='smtp.gmail.com',
        MAIL_PORT=465,
        MAIL_USE_SSL=True,
        MAIL_USERNAME='clblommberg@gmail.com',
        MAIL_PASSWORD='zvcuiforvcnxgmwy'
    )

    # Register the custom filter with Jinja2
    app.jinja_env.filters['currency'] = format_currency

    # Blueprints
    from app.admin import admin_bp
    from app.auth import auth_bp

    app.register_blueprint(admin_bp)
    app.register_blueprint(auth_bp)

    with app.app_context():
        # Inicializar la secuencia
        initialize_sequence()

    return app

def initialize_sequence():
    """Inicializa la secuencia de la tabla customer"""
    with db.engine.connect() as connection:
        connection.execute(
            text("SELECT setval('customer_cid_seq', (SELECT COALESCE(MAX(cid), 1) FROM customer))")
        )