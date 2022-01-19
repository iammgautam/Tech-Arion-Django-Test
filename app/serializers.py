from rest_framework import serializers

from .models import Profile,Address

class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = (
            'id',
            'name',
            'dateOfBirth',
            'gender',
            'phoneNumber',
        )


class AddressSerializer(serializers.ModelSerializer):
    owner = ProfileSerializer()
    class Meta:
        model = Address
        fields = (
            'owner',
            'address1',
            'address2',
            'pincode'
        )




