from django.urls import path
from .views import  AddressModelViewSet, ProfileListAPIVIew
from rest_framework import routers

router = routers.SimpleRouter()
router.register(r'profile', AddressModelViewSet, basename='profile')

urlpatterns = [
    # path('home/', home, name='homepage'),
    # path('address/', Address, name='address'),
    path("", ProfileListAPIVIew.as_view(), name='address-list',)
] + router.urls