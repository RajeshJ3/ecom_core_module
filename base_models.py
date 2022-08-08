from core.db import redis_db

class BaseModel:

    class Meta:
        database = redis_db
