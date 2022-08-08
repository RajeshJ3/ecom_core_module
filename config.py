from os import environ as env

REDIS_DB_HOST = env.get("REDIS_DB_HOST")
REDIS_DB_PORT = int(env.get("REDIS_DB_PORT", 6379))
