from rest_framework import serializers
from .models import Category, Project


class ProjectSerialiser(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.id')
    date_created = serializers.ReadOnlyField()
    class Meta:
        model = Project
        fields = '__all__'