# users/serializers.py
from rest_framework import serializers 
from .models import CustomUser


class CustomUserSerialiser(serializers.ModelSerializer):
    
    class Meta:
        model = CustomUser
        fields = ['username', 'email', 'password']

        # These fields are only editable (not displayed) and have to be a part of 'fields' tuple
        extra_kwargs = {'password': {'write_only': True, 'min_length': 4}}

        # These fields are displayed but not editable and have to be a part of 'fields' tuple
        #read_only_fields = ('is_active', 'is_staff', 'is_superuser',)


    # def create(self, validated_data):
    #     return CustomUser.objects.create(**validated_data)