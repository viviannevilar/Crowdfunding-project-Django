from rest_framework import generics, permissions, mixins, status
from .models import CustomUser
from .serialisers import CustomUserSerialiser
from crowdfunding.permissions import IsOwnerOrReadOnly


class CustomUserList(generics.ListCreateAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerialiser


class UserRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerialiser
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]
    #format = None
