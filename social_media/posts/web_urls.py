from django.urls import path
from .views import feed_view

app_name = "posts"

urlpatterns = [
    # Feed page (list of posts + create post)
    path("", feed_view, name="feed"),
]
