from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework import generics

from .models import Follow, User
from .permissions import IsAuthorOrReadOnly
from .serializers import FollowSerializer


class SubscriptionViewSet(viewsets.ModelViewSet):
    """CRUD подписки. """
    queryset = Follow.objects.all()
    serializer_class = FollowSerializer
    permission_classes = [IsAuthenticated, IsAuthorOrReadOnly]

    def get_queryset(self):
        return Follow.objects.filter(user=self.request.user)
