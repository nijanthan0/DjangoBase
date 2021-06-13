from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from django.contrib.auth.models import User, Group
from .serializers import UsersSerializer, GroupSerializer
# Create your views here.
from rest_framework.response import Response

class UserSet(ModelViewSet):
    # permission_classes = (permissions.IsAuthenticated,)
    queryset = User.objects.all()
    serializer_class = UsersSerializer


class GroupSet(ModelViewSet):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
