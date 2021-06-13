from rest_framework import routers
from .views import UserSet, GroupSet

from django.urls import path
router = routers.DefaultRouter()
#
router.register('users', UserSet)
router.register('groups', GroupSet)
urlpatterns = router.urls
# urlpatterns = [
#     path('users/', UserSet)
# ]
