from rest_framework import generics, permissions, mixins, status
from .models import Project, Pledge, Category
from .serialisers import (ProjectSerialiser, 
            ProjectDetailSerialiser,
            PledgeSerialiser,
            CategoryDetailSerialiser
            )
from .permissions import IsOwnerOrReadOnly


class ProjectList(generics.ListCreateAPIView):
    """ url: projects/ """
    queryset = Project.objects.all()
    serializer_class = ProjectSerialiser
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

#need to update this so that can only see projects that are published, unless project owner
class ProjectDetail(generics.RetrieveDestroyAPIView):
    """ url: project/<int:pk>/ """
    permission_classes = [
        permissions.IsAuthenticatedOrReadOnly,
        IsOwnerOrReadOnly]
    queryset = Project.objects.all()
    serializer_class = ProjectDetailSerialiser

#class ProjectUpdate(generics.UpdateAPIView):
    #I want people to be able to close projects
    #and to publish them (ability to create drafts), ie, can only update a project if it has not been published

class PledgeList(generics.ListCreateAPIView):
    """ url: pledges/ """
    queryset = Pledge.objects.all()
    serializer_class = PledgeSerialiser
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    #need to update this. Do I want the is_open to be a property on the serialiser or better in the model? Could also check ben's suggestion to override the save method on the model to close it after a certain amount is reached.
    def perform_create(self, serializer):
        if self.project.is_open == True:
            serializer.save(supporter=self.request.user)
            return Response(
                serializer.data,
                 status=status.HTTP_201_CREATED
            )
        else:
            return Response(error="This is project is closed", 
            status = status.HTTP_403_FORBIDDEN)



# def post(self, request):
#         serializer = ProjectSerialiser(data = request.data)
#         if serializer.is_valid():
#             serializer.save(owner=request.user)
#             return Response(
#                 serializer.data,
#                 status=status.HTTP_201_CREATED
#             )
#         return Response(
#             serializer.errors,
#             status = status.HTTP_400_BAD_REQUEST
#         )

class CategoryList(generics.ListAPIView):
    """ url: categories/ """
    queryset = Category.objects.all()
    serializer_class = CategoryDetailSerialiser


class CategoryDetail(generics.RetrieveAPIView):
    """ url: categories/<str:name>/"""
    queryset = Category.objects.all()
    serializer_class = CategoryDetailSerialiser
    lookup_field = 'name'

