from django.core.cache import cache
from .models import Property

def get_all_properties():
    # Try to get the data from Redis
    all_properties = cache.get('all_properties')
    if all_properties is None:
        # If not cached, fetch from DB and cache for 1 hour (3600 seconds)
        all_properties = list(Property.objects.all().values('id', 'title', 'description', 'price', 'location', 'created_at'))
        cache.set('all_properties', all_properties, timeout=3600)
    return all_properties
