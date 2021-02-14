import redis
from config import REDIS_HOST, REDIS_KEY, REDIS_PORT

def load_redis(app):
    app.config["SESSION_REDIS"] = redis.Redis(host=REDIS_HOST, port=REDIS_PORT, password=REDIS_KEY)
    return app