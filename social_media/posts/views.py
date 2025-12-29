from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Post, Like, Comment

@login_required
def feed_view(request):
    posts = Post.objects.all().order_by("-created_at")

    if request.method == "POST":
        if "content" in request.POST:
            Post.objects.create(
                user=request.user,
                content=request.POST.get("content")
            )

        if "like_post" in request.POST:
            post = get_object_or_404(Post, id=request.POST.get("like_post"))
            Like.objects.get_or_create(user=request.user, post=post)

        if "comment_post" in request.POST:
            post = get_object_or_404(Post, id=request.POST.get("comment_post"))
            Comment.objects.create(
                user=request.user,
                post=post,
                text=request.POST.get("comment")
            )

        return redirect("feed")

    return render(request, "posts/feed.html", {"posts": posts})
