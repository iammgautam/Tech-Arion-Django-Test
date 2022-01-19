from django import forms
from .models import Profile, Address

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('__all__')


class AddressForm(forms.ModelForm):
    class Meta:
        model = Address
        fields = ('__all__')
    