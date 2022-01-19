from dataclasses import field
from rest_framework import serializers

from .models import Profile,Address

class AddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = Address
        fields = ('__all__')

class ProfileSerializer(serializers.ModelSerializer):
    address = AddressSerializer()
    class Meta:
        model = Profile
        fields = (
            'id',
            'name',
            'dateOfBirth',
            'gender',
            'phoneNumber',
            'address',
        )



