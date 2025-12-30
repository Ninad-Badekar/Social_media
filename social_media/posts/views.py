from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required

from rest_framework import generics, permissions, status
from rest_framework.views import APIView
from rest_framework.response import Response

from .models import Post, Comment, Like
from .serializers import PostSerializer, CommentSerializer, LikeSerializer

@login_required
def feed_view(request):
    posts = Post.objects.all().order_by("-created_at")

    if request.method == "POST":

        # Create Post
        if "content" in request.POST:
            Post.objects.create(
                author=request.user,
                content=request.POST.get("content")
            )

        # Like Post
        if "like_post" in request.POST:
            post = get_object_or_404(Post, id=request.POST.get("like_post"))
            Like.objects.get_or_create(
                user=request.user,
                post=post
            )

        # Comment on Post
        if "comment_post" in request.POST:
            post = get_object_or_404(Post, id=request.POST.get("comment_post"))
            Comment.objects.create(
                user=request.user,
                post=post,
                text=request.POST.get("comment")
            )

        return redirect("feed")

    return render(request, "posts/feed.html", {"posts": posts})

class PostListCreateAPI(generics.ListCreateAPIView):
    queryset = Post.objects.all().order_by("-created_at")
    serializer_class = PostSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)
class PostRetrieveUpdateDeleteAPI(generics.RetrieveUpdateDestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [permissions.IsAuthenticated]

class CommentListCreateAPI(generics.ListCreateAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

class CommentRetrieveUpdateDeleteAPI(generics.RetrieveUpdateDestroyAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [permissions.IsAuthenticated]

class LikeAPI(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request):
        Like.objects.get_or_create(
            user=request.user,
            post_id=request.data.get("post")
        )
        return Response(
            {"message": "Post liked"},
            status=status.HTTP_201_CREATED
        )

    def delete(self, request):
        Like.objects.filter(
            user=request.user,
            post_id=request.data.get("post")
        ).delete()
        return Response(
            {"message": "Like removed"},
            status=status.HTTP_204_NO_CONTENT
        )
