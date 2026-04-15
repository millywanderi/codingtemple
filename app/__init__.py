#!/usr/bin/env python3

#Setup Swagger in app/__init__.py to access documentation & test APIs
from flask_swagger_ui import get_swaggerui_blueprint

SWAGGER_URL = '/api/docs'
API_URL = 'static/swagger.yaml'

swaggerui_blueprint = get_swaggerui_blueprint(
    SWAGGER_URL,
    API_URL,
    config={
        'Library API':
    }
)

def create_app(config_name):

    app = Flask(__name__)
    app.config.from_object(f"config.{config_name}")

    #Add extensions to app
    db.init_app(app)
    ma.init_app(app)
    limiter.init_app(app)
    cache.init_app(app)

    # registering blueprints
    app.register_blueprint(members_bp, url_prefix='/members')
    app.register_blueprint(books_bp, url_prefix='/books')
    app.register_blueprint(loan_bp, url_prefix='/loans')
    app.register_blueprint(items_bp, url_prefix='/items')
    app.register_blueprint(orders_bp, url_prefix='/orders')
    app.register_blueprint(swagger_blueprint, url_prefix=SWAGGER_URL)

    return app
