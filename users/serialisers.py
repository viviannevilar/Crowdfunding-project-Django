# users/serializers.py
from rest_framework import serializers 
from django.contrib.auth import get_user_model
from projects.serialisers import PledgeSerialiser

User = get_user_model()

class CustomUserSerialiser(serializers.ModelSerializer):
  
    class Meta:
        model = User
        fields = ('username', 'email', 'password')
        lookup_field = 'username'

        # These fields are only editable (not displayed) and have to be a part of 'fields' tuple
        extra_kwargs = {'password': {'write_only': True, 'min_length': 4}}

        # These fields are displayed but not editable and have to be a part of 'fields' tuple
        #read_only_fields = ('is_active', 'is_staff', 'is_superuser',)


    # def create(self, validated_data):
    #     return User.objects.create(**validated_data)

    # 
    # def create(self, validated_data):
    #     user = super(CustomUserSerialiser, self).create(validated_data)
    #     user.set_password(validated_data['password'])
    #     user.save()
    #     return user

class UserDisplaySerialiser(CustomUserSerialiser):
    pledges = PledgeSerialiser(many=True, read_only=True)

class UserProfileSerialiser(serializers.ModelSerializer):
    pledges = PledgeSerialiser(many=True, read_only=True)

    class Meta:
        model = User
        fields = '__all__'

  

