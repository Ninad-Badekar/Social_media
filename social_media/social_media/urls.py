from django.contrib import admin
from django.urls import path, include
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView

schema_view = get_schema_view(
    openapi.Info(
        title="Social Media Platform API",
        default_version="v1",
        description="Django Social Media App with Web UI and REST APIs",
    ),
    public=True,
    permission_classes=[permissions.AllowAny],
)

urlpatterns = [
    # Django Admin
    path("admin/", admin.site.urls),

    # Web UI (HTML)
    path("", include("posts.web_urls")),     # Feed page `/`
    path("", include("users.web_urls")), # Login / Register / Logout

    # REST APIs
    path("api/", include("posts.urls")),
    path("api/", include("follows.urls")),
    path("api/", include("users.urls")),

    path("api/schema/", SpectacularAPIView.as_view(), name="schema"),
    path("swagger/", SpectacularSwaggerView.as_view(url_name="schema"), name="swagger-ui"),

]
