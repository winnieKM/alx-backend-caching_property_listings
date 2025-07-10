import logging
from django_redis import get_redis_connection

logger = logging.getLogger(__name__)

def get_redis_cache_metrics():
    """
    Retrieves Redis cache hit/miss metrics and calculates hit ratio.
    Logs the results and returns them in a dictionary.
    """
    conn = get_redis_connection("default")
    info = conn.info()

    hits = info.get("keyspace_hits", 0)
    misses = info.get("keyspace_misses", 0)
    total = hits + misses

    hit_ratio = (hits / total) if total > 0 else 0

    logger.info(f"Redis Cache Metrics -> Hits: {hits}, Misses: {misses}, Hit Ratio: {hit_ratio:.2%}")

    return {
        "hits": hits,
        "misses": misses,
        "hit_ratio": round(hit_ratio, 2),
    }
