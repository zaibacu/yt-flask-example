import os

from flask import Flask


from routes.admin import bp as admin_bp
from routes.site import bp as site_bp
from routes.health import bp as health_bp

from database import db

app = Flask('example')

app.register_blueprint(admin_bp, url_prefix='/admin')
app.register_blueprint(site_bp)
app.register_blueprint(health_bp, url_prefix='/-/')

app.config.from_object(os.getenv('FLASK_CONFIG', 'config.DevConfig'))

db.init_app(app)

if __name__ == '__main__':
    app.run()
