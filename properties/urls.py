from django.urls import path
from .views import property_list, redis_metrics

urlpatterns = [
    path('', property_list, name='property_list'),
    path('metrics/', redis_metrics, name='redis_metrics'),
]
