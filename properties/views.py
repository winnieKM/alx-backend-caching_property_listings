from django.http import JsonResponse
from django.views.decorators.cache import cache_page
from .utils import get_all_properties  # ✅ import the new utility function

@cache_page(60 * 15)  # Cache full response for 15 minutes
def property_list(request):
    properties = get_all_properties()  # ✅ Use low-level cache function
    return JsonResponse({
        "data": properties
    })
