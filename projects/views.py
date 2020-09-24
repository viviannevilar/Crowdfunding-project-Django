from rest_framework import generics, permissions, mixins, status
from .models import Project, Pledge, Category, Favourite
from .serialisers import (ProjectSerialiser, 
            ProjectDetailSerialiser,
            ProjectPublishSerialiser,
            PledgeSerialiser,
            CategoryDetailSerialiser,
            FavouriteSerialiser
            )
from .permissions import IsOwnerOrReadOnly, IsOwnerDraft
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.filters import OrderingFilter, SearchFilter
from django_filters.rest_framework import DjangoFilterBackend
from django.http import Http404, HttpResponseForbidden
from .filters import DynamicSearchFilter
from django.utils import timezone



class ProjectList(generics.ListCreateAPIView):
    """ 
    Shows all published projects
    url: projects/ 
    """
    queryset = Project.objects.filter(pub_date__isnull=False)
    serializer_class = ProjectSerialiser
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    filter_backends = [OrderingFilter, DjangoFilterBackend, DynamicSearchFilter]#SearchFilter]

    ordering_fields = ['category', 'pub_date', 'goal']
    filterset_fields = ['owner','category', 'pub_date']
    #search_fields = ['description', 'title', 'owner__username', 'category__name']

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class OwnerProjectList(generics.ListCreateAPIView):
    """ 
    shows all projects (including drafts) belonging to the user making the request, allows creation of projects
    url: myprojects/ 
    QUESTION: do I need any extra permissions here? The filtering only shows projects from request user, but do I need to worry about someone seeing the projects from someone else?
    """
    serializer_class = ProjectSerialiser
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    filter_backends = [OrderingFilter, DjangoFilterBackend]
    ordering_fields = ['goal', 'pub_date']
    filterset_fields = ['owner','category', 'pub_date']

    def get_queryset(self):
        return Project.objects.filter(owner=self.request.user)

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

class ProjectDetail(generics.RetrieveUpdateDestroyAPIView):
    """ 
    url: project/<int:pk>/
    only owners can see drafts and delete projects
    """
    permission_classes = [IsOwnerDraft,]
    queryset = Project.objects.all()
    serializer_class = ProjectDetailSerialiser





# class ProjectPublishSet(viewsets.ModelViewSet):
#     """
#     A viewset that provides the standard actions
#     """
#     queryset = Project.objects.all()
#     serializer_class = ProjectPublishSerialiser


#     @action(detail=True, methods=['post'])
#     def set_pub_date(self, request, pk=None):
#         project = self.get_object()
#         serializer = ProjectPublishSerialiser(data=request.data)
#         if serializer.is_valid():
#             project.pub_date = timezone.now()]
#             project.save()
#             return Response({'status': 'project published'})
#         else:
#             return Response(serializer.errors,
#                             status=status.HTTP_400_BAD_REQUEST)


class ProjectPublish(APIView):
    "publish project"
    permission_classes = [IsOwnerDraft,]
    queryset = Project.objects.all()
    # serializer_class = ProjectPublishSerialiser

    def get_object(self, pk):
        try:
            return Project.objects.get(pk=pk)
        except Project.DoesNotExist:
            raise Http404

    def post(self, request, pk):
        project = self.get_object(pk)
        self.check_object_permissions(request, project)        
        data = request.data
        project.pub_date = timezone.now()
        project.save()
        return Response({'status': 'project published'})



class PledgeList(APIView):
    """ 
    creates pledges for a given project, if the project is open

    url: pledges/ """
    def get(self, request):
        pledges = Pledge.objects.all()
        serializer = PledgeSerialiser(pledges, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = PledgeSerialiser(data = request.data)
        if serializer.is_valid():
            project_pk = request.data['project']
            project_object = Project.objects.get(pk = project_pk)
            #print(project_object.is_open)
            if project_object.is_open and (project_object.owner != self.request.user):
                serializer.save(supporter=self.request.user)
                return Response(
                    serializer.data,
                    status=status.HTTP_201_CREATED
                )
            elif project_object.owner == self.request.user:
                return Response({"detail": "You can't donate to your own projects!"}, status=status.HTTP_400_BAD_REQUEST
            )
            return Response({"detail": "This project is closed"}, status=status.HTTP_400_BAD_REQUEST
            )
            
        return Response(
            serializer.errors,
            status=status.HTTP_400_BAD_REQUEST
        )


class CategoryList(generics.ListAPIView):
    """ url: categories/ """
    queryset = Category.objects.all()
    serializer_class = CategoryDetailSerialiser


class CategoryDetail(generics.RetrieveAPIView):
    """ url: categories/<str:name>/"""
    queryset = Category.objects.all()
    serializer_class = CategoryDetailSerialiser
    lookup_field = 'name'


#only person can favourite stuff to their own account
class FavouriteListView(generics.ListCreateAPIView):
    """ 
    shows all favourites belonging to the request user
    if favourite exists, remove, otherwise create
    url: favourites 
    """
    serializer_class = FavouriteSerialiser
    permission_classes = [IsOwnerOrReadOnly]

    def get_queryset(self):
        """
        This view should return a list of all favourites for the currently authenticated user.
        """
        user = self.request.user
        return Favourite.objects.filter(owner=user)

    def perform_create(self, serializer):
        print(serializer.validated_data)
        serializer.is_valid()
        # do it first ^^^^^
        data = serializer.validated_data
        project = data.get('project')
        user = self.request.user
        if project.favouriters.filter(id=user.id).exists():
            project.favouriters.remove(user)
        else:
            project.favouriters.add(user)


class FavouriteView(APIView):
    """
    See if the project (url has id of project) has been liked by current user (request.user). If yes, true, else, false.
    If posts an empty request and the favourite doesn't exist, it will be created, otherwise it will remove it

    """

    def get_object(self, pk):
        try:
            return Project.objects.get(pk=pk)
        except Project.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        favourited = False
        project = self.get_object(pk)
        user = request.user
        if project.favouriters.filter(id=user.id).exists():
            favourited = True
        return Response(f"{project},{user},{favourited}")

    def post(self, request, pk):
        project = self.get_object(pk)
        if project.favouriters.filter(id=request.user.id).exists():
            project.favouriters.remove(request.user)
            favourited = False
        else:
            post.favourites.add(request.user)
            favourited = True
        












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


