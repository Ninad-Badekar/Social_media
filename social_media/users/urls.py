from django.urls import path
from .api_views import (
    UserRegisterAPI,
    UserProfileAPI,
)

urlpatterns = [
    # Register new user (API)
    path("users/register/", UserRegisterAPI.as_view(), name="api-register"),

    # Get logged-in user profile
    path("users/me/", UserProfileAPI.as_view(), name="api-profile"),
]
