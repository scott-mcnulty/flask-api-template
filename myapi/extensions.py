from flask_sqlalchemy import SQLAlchemy
from flask_jwt_extended import JWTManager
from flask_marshmallow import Marshmallow
from flask_migrate import Migrate
from flask_caching import Cache
from flask_cors import CORS
from prometheus_flask_exporter import PrometheusMetrics

db = SQLAlchemy()
jwt = JWTManager()
ma = Marshmallow()
migrate = Migrate()
cache = Cache()
cors = CORS()
metrics = PrometheusMetrics(app=None)
