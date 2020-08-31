from rest_framework import generics, permissions, mixins, status
from .serialisers import (
    CustomUserSerialiser, 
    UserProfileSerialiser,
    UserDisplaySerialiser)
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


#register uses a serialiser that only requires two (or three) fields. The update profile will have more fields.
class UserCreate(generics.CreateAPIView):
    """ url: users/register/ """
    queryset = User.objects.all()
    serializer_class = CustomUserSerialiser


class UserRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = CustomUserSerialiser
    permission_classes = (permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly,)
    lookup_field = 'username'
    

# class UserProfile(generics.RetrieveAPIView):
#     """ This is trying to show different information (different serialiser) depending on whether the request user is the owner of that profile """

#     queryset = User.objects.all()
#     lookup_field = 'username'

#     def get_serializer_class(self):
#         if self.request.user == self.get_object():
#             return UserProfileSerialiser
#         return UserDisplaySerialiser




class UserProfile(APIView):

    def get_object(self, pk):
        try:
            return User.objects.get(pk=pk)
        except User.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        user = self.get_object(pk)
        if request.user == user:
            serializer = UserProfileSerialiser(user)
        else:
            serializer = UserDisplaySerialiser(user)
        return Response(serializer.data)



