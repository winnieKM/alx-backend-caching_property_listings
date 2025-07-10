from django.http import JsonResponse
from .utils import get_redis_cache_metrics

def redis_metrics(request):
    metrics = get_redis_cache_metrics()
    return JsonResponse(metrics)
