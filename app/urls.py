from django.urls import path
from .views import  ProfileModelViewSet, AddressListAPIVIew
from rest_framework import routers

router = routers.SimpleRouter()
router.register(r'profile', ProfileModelViewSet, basename='profile')

urlpatterns = [
    # path('home/', home, name='homepage'),
    # path('address/', Address, name='address'),
    path("api/address", AddressListAPIVIew.as_view(), name='address',)
] + router.urls