from django.shortcuts import render

from rest_framework import generics, permissions
from .models import Follow
from .serializers import FollowSerializer

class FollowCreateAPI(generics.CreateAPIView):
    queryset = Follow.objects.all()
    serializer_class = FollowSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(follower=self.request.user)
