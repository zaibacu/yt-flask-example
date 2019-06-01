from flask import Flask

from routes.admin import bp as admin_bp
from routes.site import bp as site_bp
from routes.health import bp as health_bp

app = Flask('example')

app.register_blueprint(admin_bp, url_prefix='/admin')
app.register_blueprint(site_bp)
app.register_blueprint(health_bp, url_prefix='/-/')

app.run(debug=True)
