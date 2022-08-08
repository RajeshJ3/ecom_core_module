from redis_om import get_redis_connection

from core.config import (
    REDIS_DB_HOST,
    REDIS_DB_PORT
)

redis_db = get_redis_connection(
    host=REDIS_DB_HOST,
    port=REDIS_DB_PORT,
    decode_responses=True
)
