from rest_framework import generics, permissions, mixins, status
from .serialisers import (
    CustomUserSerialiser, 
    UserProfileSerialiser,
    UserDisplaySerialiser,
    UserSerialiser)
from .permissions import IsOwnerOrReadOnly
from django.contrib.auth import get_user_model
from rest_framework.views import APIView

from django.http import Http404
from rest_framework.response import Response

User = get_user_model()

class UserList(generics.ListAPIView):
    """ url: users/ """
    queryset = User.objects.all()
    serializer_class = CustomUserSerialiser


class UserCreate(generics.CreateAPIView):
    """ url: users/register/ """
    queryset = User.objects.all()
    serializer_class = CustomUserSerialiser


class UserRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    """ url: '<str:username>/' """
    
    queryset = User.objects.all()
    serializer_class = UserSerialiser
    permission_classes = (permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly,)
    lookup_field = 'username'


class UserProfile(generics.RetrieveAPIView):
    """ 
    url: '<str:username>/profile/'
    User profile. Shows pledges and projects depending on whether the user is the owner of the account or not.
    """
    queryset = User.objects.all()
    lookup_field = 'username'

    def get_serializer_class(self):
        if self.request.user == self.get_object():
            return UserProfileSerialiser
        return UserDisplaySerialiser
