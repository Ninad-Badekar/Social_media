from django.urls import path
from .views import (
    feed_view,
    PostListCreateAPI,
    PostRetrieveUpdateDeleteAPI,
    CommentListCreateAPI,
    CommentRetrieveUpdateDeleteAPI,
    LikeAPI,
)

urlpatterns = [
    # Web UI
    path("", feed_view, name="feed"),

    # APIs
    path("posts/", PostListCreateAPI.as_view()),
    path("posts/<int:pk>/", PostRetrieveUpdateDeleteAPI.as_view()),

    path("comments/", CommentListCreateAPI.as_view()),
    path("comments/<int:pk>/", CommentRetrieveUpdateDeleteAPI.as_view()),

    path("likes/", LikeAPI.as_view()),
]
