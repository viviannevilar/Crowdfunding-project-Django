from rest_framework import serializers
from .models import Category, Project, Pledge, Favourite
from django.utils.timezone import now
from datetime import datetime, timedelta

class ProjectSerialiser(serializers.ModelSerializer):
    #owner = serializers.ReadOnlyField(source='owner.id')
    owner = serializers.ReadOnlyField(source='owner.username')
    #owner = serializers.HyperlinkedRelatedField(read_only=True, view_name = 'id', lookup_field='id')
    date_created = serializers.ReadOnlyField()
    is_open = serializers.ReadOnlyField()
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

 
    # def create(self, validated_data):
    #     """create a new pledge"""

    #     supporter = validated_data['supporter.username']
    #     amount = validated_data['amount']
    #     comment = validated_data['comment']
    #     anonymous = validated_data['anonymous']
    #     project = validated_data['project']
        
    #     project_object = Project.objects.get(pk = project)
    #     if project_object.is_open:
    #         pledge = Pledge.object.create(
    #             supporter = supporter,
    #             amount = amount,
    #             comment = comment,
    #             anonymous = anonymous,
    #             project = project
    #         )
    #     else:
    #         raise serializers.ValidationError({'message': "Project is closed"})
       



class ProjectDetailSerialiser(ProjectSerialiser):
    project_pledges = PledgeSerialiser(many=True, read_only=True)



#from django.utils.text import slugify

#https://stackoverflow.com/questions/56015369/slug-field-in-django-rest-framework
# class CatSlugSerializer(serializers.ModelSerializer):
#     name_slug = serializers.SerializerMethodField()

#     def get_name_slug(self, instance):
#         return slugify(instance.name)

#     class Meta:
#         model = Category
#         fields = ("name_slug", )



class CategorySerialiser(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'
        lookup_field = 'name'
        # extra_kwargs = {
        #     'url': {'lookup_field': 'name'}
        # }

"""
data = {
    "name": "delete",
    "description": "testing the shell"
}

new_item = CategorySerialiser(data=data)

if new_item.is_valid():
    new_item.save()
else:
    print(new_item.errors)
"""

class CategoryDetailSerialiser(CategorySerialiser):
    cat_projects = ProjectSerialiser(many=True, read_only=True)
    



class PledgeUserSerialiser(serializers.ModelSerializer):
    """ used by the UserProfile view, to show info on a specific user """
    #supporter = serializers.ReadOnlyField(source='supporter.username')
    date_sent = serializers.ReadOnlyField()
     
    class Meta:
        model = Pledge
        fields = '__all__'

class ProjectUserSerialiser(serializers.ModelSerializer):
    """" used by the UserProfile view, to show info on a specific user """
    #supporter = serializers.ReadOnlyField(source='supporter.username')
    
    class Meta:
        model = Project
        exclude = ['owner']


class FavouriteSerialiser(serializers.ModelSerializer):
    """ used by FavouriteListView """
    date = serializers.ReadOnlyField()

    class Meta:
        model = Favourite
        fields = '__all__'

#https://stackoverflow.com/questions/42321011/user-dependent-field-as-many-to-many-relationship-in-django-rest-framework`
# class FavoriteField(serializers.BooleanField):

#     def get_attribute(self, instance):
#         pk = instance.pk
#         project = Project.objects.get(pk=pk)
#         return project.favouriters.filter(id=self.context['request'].user.id).exists()


# class FavProductSerializer(serializers.ModelSerializer):
#     favorite = FavoriteField()

#     def update(self, instance, validated_data):
#         instance = super().update(instance, validated_data)
#         is_favourite = validated_data.get('favorite')  # can be None
#         if is_favourite is True:
#             instance.favouriters.remove(self.context['request'].user.id)
#         elif is_favourite is False:
#             instance.favouriters.add(self.context['request'].user.id)
#         return instance