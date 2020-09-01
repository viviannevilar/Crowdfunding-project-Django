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


#register uses a serialiser that only requires two (or three) fields. The update profile will have more fields.
class UserCreate(generics.CreateAPIView):
    """ url: users/register/ """
    queryset = User.objects.all()
    serializer_class = CustomUserSerialiser


class UserRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    """ url: '<str:username>/' 
    maybe this should be deleted? """
    
    queryset = User.objects.all()
    serializer_class = UserSerialiser
    permission_classes = (permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly,)
    lookup_field = 'username'
    
    # This here is to be able to do partial update, but it seems to work without it
    # def get_serializer(self, *args, **kwargs):
    #     kwargs['partial'] = True
    #     return super(UserRetrieveUpdateDestroy, self).get_serializer(*args, **kwargs)


#need to update this so as not to have the supporter show in the pledge bit of the info about the user
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


# class UserProfile(APIView):
# """ does the same thing as the above, but using APIView """
#     def get_object(self, pk):
#         try:
#             return User.objects.get(pk=pk)
#         except User.DoesNotExist:
#             raise Http404

#     def get(self, request, pk):
#         user = self.get_object(pk)
#         if request.user == user:
#             serializer = UserProfileSerialiser(user)
#         else:
#             serializer = UserDisplaySerialiser(user)
#         return Response(serializer.data)



# Reset Password?