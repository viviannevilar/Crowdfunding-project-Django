from rest_framework import serializers
from .models import Category, Project, Pledge


class ProjectSerialiser(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.id')
    date_created = serializers.ReadOnlyField()
    class Meta:
        model = Project
        fields = '__all__'


class PledgeSerialiser(serializers.ModelSerializer):
    supporter = serializers.ReadOnlyField(source='supporter.id')
    date_sent = serializers.ReadOnlyField()
    
    class Meta:
        model: Pledge
        fields = '__all__'

 
class ProjectDetailSerialiser(ProjectSerialiser):
    pledges = PledgeSerialiser(many=True, read_only=True)

    #how to make sure a pledge is only created when viewing a project, and the project's id is automatically added?

class CategorySerialiser(serializers.Serializer):
    projects = ProjectSerialiser(many=True, read_only=True)

    class Meta:
        model: Category
        fields: "__all__"