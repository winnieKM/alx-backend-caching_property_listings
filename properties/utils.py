import logging
from django.core.cache import cache

logger = logging.getLogger(__name__)

def get_redis_cache_metrics():
    try:
        client = cache.client.get_client(write=False)
        info = client.info()

        hits = info.get('keyspace_hits', 0)
        misses = info.get('keyspace_misses', 0)
        total_requests = hits + misses
        hit_ratio = hits / total_requests if total_requests > 0 else 0

        logger.info(f"Redis cache metrics - Hits: {hits}, Misses: {misses}, Hit Ratio: {hit_ratio:.2f}")

        return {
            'hits': hits,
            'misses': misses,
            'hit_ratio': hit_ratio,
        }

    except Exception as e:
        logger.error(f"Error retrieving Redis cache metrics: {e}")
        return {
            'hits': 0,
            'misses': 0,
            'hit_ratio': 0,
        }
