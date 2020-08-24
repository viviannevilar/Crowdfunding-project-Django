from rest_framework import generics, permissions, mixins, status
from .models import Project
from .serialisers import ProjectSerialiser

# Create your views here.
class ProjectList(generics.ListCreateAPIView):
    queryset = Project.objects.all()
    serializer_class = ProjectSerialiser
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)