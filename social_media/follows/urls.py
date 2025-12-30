from django.urls import path
from .views import FollowCreateAPI

urlpatterns = [
    path('api/follow/', FollowCreateAPI.as_view(), name='follow-api'),
]
