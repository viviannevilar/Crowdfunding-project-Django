from rest_framework import generics, permissions, mixins, status
from .serialisers import CustomUserSerialiser
from .permissions import IsOwnerOrReadOnly
from django.contrib.auth import get_user_model

User = get_user_model()

class UserList(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = CustomUserSerialiser

class UserRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = CustomUserSerialiser
    permission_classes = (permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly,)

class UserCreate(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = CustomUserSerialiser
    #permission_classes = (AllowAny,)