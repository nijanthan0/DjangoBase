
from rest_framework import serializers
from django.contrib.auth.models import User, Group


class UsersSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = '__all__'

class GroupSerializer(serializers.ModelSerializer):

    class Meta:
        model = Group
        fields = '__all__'