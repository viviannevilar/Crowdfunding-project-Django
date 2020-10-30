from rest_framework import serializers
from .models import Category, Project, Pledge, Favourite
from django.utils.timezone import now
from datetime import datetime, timedelta
from django.utils import timezone

class ProjectSerialiser(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    date_created = serializers.ReadOnlyField()
    is_open = serializers.ReadOnlyField()
    tot_donated = serializers.ReadOnlyField()
    fav_count = serializers.SerializerMethodField()

    class Meta:
        model = Project
        fields = '__all__'

    def get_fav_count(self,obj):
        return obj.favouriters.count()


class PledgeSerialiser(serializers.ModelSerializer):
    supporter = serializers.ReadOnlyField(source='supporter.username')
    date_sent = serializers.ReadOnlyField()
    #project = serializers.ReadOnlyField()
    
    class Meta:
        model = Pledge
        fields = '__all__'


class PledgeProjSerialiser(serializers.ModelSerializer):
    supporter = serializers.ReadOnlyField(source='supporter.username')
    date_sent = serializers.ReadOnlyField()
    #project = serializers.ReadOnlyField()
    
    class Meta:
        model = Pledge
        exclude = 'project'


class ProjectDetailSerialiser(ProjectSerialiser):
    project_pledges = PledgeSerialiser(many=True, read_only=True)


class ProjectPublishSerialiser(serializers.ModelSerializer):

    class Meta:
        model = Project
        fields = "pub_date"


class CategorySerialiser(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'
        lookup_field = 'name'


class CategoryDetailSerialiser(CategorySerialiser):
    cat_projects = ProjectSerialiser(many=True, read_only=True)
    

class PledgeUserSerialiser(serializers.ModelSerializer):
    """ used by the UserProfile view, to show info on a specific user """

    date_sent = serializers.ReadOnlyField()
     
    class Meta:
        model = Pledge
        fields = '__all__'


class ProjectUserSerialiser(serializers.ModelSerializer):
    """" used by the UserProfile view, to show info on a specific user """
    
    class Meta:
        model = Project
        exclude = ['owner']


class FavouriteSerialiser(serializers.ModelSerializer):
    """ used by FavouriteListView """
    date = serializers.ReadOnlyField()

    class Meta:
        model = Favourite
        fields = '__all__'
        read_only_fields = ('owner',)

