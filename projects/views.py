from rest_framework import generics, permissions, mixins, status
from .models import Project, Pledge, Category
from .serialisers import (ProjectSerialiser, 
            ProjectDetailSerialiser,
            PledgeSerialiser,
            CategoryDetailSerialiser
            )
from .permissions import IsOwnerOrReadOnly
from rest_framework.response import Response
from rest_framework.views import APIView

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


class PledgeList(APIView):

    def get(self, request):
        pledges = Pledge.objects.all()
        serializer = PledgeSerialiser(pledges, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = PledgeSerialiser(data = request.data)
        if serializer.is_valid():
            project_pk = request.data['project']
            project_object = Project.objects.get(pk = project_pk)
            print(project_object.is_open)
            if project_object.is_open:
                serializer.save(supporter=self.request.user)
                return Response(
                    serializer.data,
                    status=status.HTTP_201_CREATED
                )
            return Response({"detail": "This project is closed"}, status=status.HTTP_400_BAD_REQUEST
            )
            
        return Response(
            serializer.errors,
            status=status.HTTP_400_BAD_REQUEST
        )

#this was to do the same as the above using generic views, but it is not working (the error message isn't working, but it is performing correctly)
# class PledgeList(generics.ListCreateAPIView):
#     """ url: pledges/ """
#     queryset = Pledge.objects.all()
#     serializer_class = PledgeSerialiser
#     permission_classes = [permissions.IsAuthenticatedOrReadOnly]

#     # def perform_create(self,serializer):
#     #     serializer.save(supporter=self.request.user)

#     #need to update this. Do I want the is_open to be a property on the serialiser or better in the model? Could also check ben's suggestion to override the save method on the model to close it after a certain amount is reached.
#     def perform_create(self, serializer):
#         project_pk = serializer.data['project']
#         print(project_pk)
#         project = Project.objects.get(pk = project_pk)
#         print(project)
        # print(project.is_open)
        # if project.is_open:
        #     serializer.save(supporter=self.request.user)
        #     return Response(
        #         serializer.data,
        #          status=status.HTTP_201_CREATED
        #     )
        # return Response({"detail": "This project is closed"}, status=status.HTTP_400_BAD_REQUEST)



class CategoryList(generics.ListAPIView):
    """ url: categories/ """
    queryset = Category.objects.all()
    serializer_class = CategoryDetailSerialiser


class CategoryDetail(generics.RetrieveAPIView):
    """ url: categories/<str:name>/"""
    queryset = Category.objects.all()
    serializer_class = CategoryDetailSerialiser
    lookup_field = 'name'

