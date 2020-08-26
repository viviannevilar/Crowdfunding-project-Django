from rest_framework import generics, permissions, mixins, status
from .models import Project, Pledge, Category
from .serialisers import (ProjectSerialiser, 
            ProjectDetailSerialiser,
            PledgeSerialiser,
            CategorySerialiser
            )
from .permissions import IsOwnerOrReadOnly

# Create your views here.
class ProjectList(generics.ListCreateAPIView):
    queryset = Project.objects.all()
    serializer_class = ProjectSerialiser
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

class ProjectDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [
        permissions.IsAuthenticatedOrReadOnly,
        IsOwnerOrReadOnly]
    queryset = Project.objects.all()
    serializer_class = ProjectDetailSerialiser

class PledgeList(generics.ListAPIView):
    queryset = Pledge.objects.all()
    serializer_class = PledgeSerialiser

class CategoryDetail(generics.RetrieveAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerialiser