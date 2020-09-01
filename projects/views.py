from rest_framework import generics, permissions, mixins, status
from .models import Project, Pledge, Category, Favourite
from .serialisers import (ProjectSerialiser, 
            ProjectDetailSerialiser,
            PledgeSerialiser,
            CategoryDetailSerialiser,
            FavouriteSerialiser
            )
from .permissions import IsOwnerOrReadOnly
from rest_framework.response import Response
from rest_framework.views import APIView
#from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import OrderingFilter
import django_filters
from django_filters import rest_framework as filters

#ordering is working, filters is not
class ProjectList(generics.ListCreateAPIView):
    """ url: projects/ """
    queryset = Project.objects.all()
    serializer_class = ProjectSerialiser
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    filter_backends = [OrderingFilter, filters.DjangoFilterBackend,]
    ordering_fields = ['category', 'date_created']
    filterset_fields = ['category', 'date_created']

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
    """ url: pledges/ """
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

# this was to do the same as the above using generic views, but it is not working (the error message isn't working, but it is performing correctly)
# maybe this will help: 
# https://www.revsys.com/tidbits/custom-exceptions-django-rest-framework/

# class PledgeList(generics.ListCreateAPIView):
#     """ url: pledges/ """
#     queryset = Pledge.objects.all()
#     serializer_class = PledgeSerialiser
#     permission_classes = [permissions.IsAuthenticatedOrReadOnly]

#     # def perform_create(self,serializer):
#     #     serializer.save(supporter=self.request.user)


    # def perform_create(self, serializer):
    #     project_pk = serializer.data['project']
    #     print(project_pk)
    #     project = Project.objects.get(pk = project_pk)
    #     print(project)
    #     print(project.is_open)
    #     if project.is_open:
    #         serializer.save(supporter=self.request.user)
    #         return Response(
    #             serializer.data,
    #              status=status.HTTP_201_CREATED
    #         )
    #     return Response({"detail": "This project is closed"}, status=status.HTTP_400_BAD_REQUEST)



class CategoryList(generics.ListAPIView):
    """ url: categories/ """
    queryset = Category.objects.all()
    serializer_class = CategoryDetailSerialiser


class CategoryDetail(generics.RetrieveAPIView):
    """ url: categories/<str:name>/"""
    queryset = Category.objects.all()
    serializer_class = CategoryDetailSerialiser
    lookup_field = 'name'


# class FavouriteView(APIView):

#     permission_classes = [
#         permissions.IsAuthenticatedOrReadOnly,
#         IsOwnerOrReadOnly]

#     def get_object(self, pk):
#         try:
#             return Project.objects.get(pk=pk)
#         except Project.DoesNotExist:
#             raise Http404
        
#     def get(self, request, pk):
#         project = self.get_object(pk)
#         serializer = ProjectDetailSerialiser(project)
#         return Response(serializer.data)

 




# class SnippetDetail(APIView):
#     """
#     Retrieve, update or delete a snippet instance.
#     """
#     def get_object(self, pk):
#         try:
#             return Snippet.objects.get(pk=pk)
#         except Snippet.DoesNotExist:
#             raise Http404

#     def get(self, request, pk, format=None):
#         snippet = self.get_object(pk)
#         serializer = SnippetSerializer(snippet)
#         return Response(serializer.data)

#     def put(self, request, pk, format=None):
#         snippet = self.get_object(pk)
#         serializer = SnippetSerializer(snippet, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#     def delete(self, request, pk, format=None):
#         snippet = self.get_object(pk)
#         snippet.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)





class FavouriteListView(generics.ListCreateAPIView):
    """ url: favourites """
    serializer_class = FavouriteSerialiser

    def get_queryset(self):
        """
        This view should return a list of all favourites for the currently authenticated user.
        """
        user = self.request.user
        return Favourite.objects.filter(owner=user)

    # need to ensure someone doesnt favourite a project more than once. 

    # Can either make a new favourite mean a removal of the favourite or just be able to remove a favourite with remove. But I like the "favourite again means remove" option



# Search?


