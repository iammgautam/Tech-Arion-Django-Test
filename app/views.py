from django.shortcuts import redirect, render
from .models import Profile, Address
from .forms import ProfileForm, AddressForm
from .serializers import ProfileSerializer, AddressSerializer
from rest_framework.viewsets import ModelViewSet
from rest_framework.generics import ListAPIView
from rest_framework.filters import OrderingFilter, SearchFilter
# Create your views here.

# def home(request):
#     if request.method == 'POST':
#         fm = ProfileForm(request.POST)
#         if fm.is_valid():
#             Name = fm.cleaned_data['name']
#             Dob = fm.cleaned_data['dateOfBirth']
#             gender = fm.cleaned_data['gender']
#             number = fm.cleaned_data['phoneNumber']
#             reg = Profile(name=Name, dateOfBirth= Dob,gender=gender, phoneNumber=number)
#             reg.save()
#             fm = ProfileForm()
        
#             return redirect(request.path)
#     else:
#         fm = ProfileForm()
    
#     context = {
#         'profile_form': fm,
#     }

#     return render(request, 'app/main.html', context)
        
# def Address(request):
#     if request.method == 'POST':
#         add = AddressForm(request.POST)
#         if add.is_valid():
#             owner = add.cleaned_data['owner']
#             add1 = add.cleaned_data['address1']
#             add2 = add.cleaned_data['address2']
#             pin = add.cleaned_data['pincode']
#             regAdd = Address(owner=owner,address1=add1, address2=add2, pincode=pin)
#             regAdd.save()
#             add = AddressForm()
#             return redirect('/homepage/')
#     else:
#         add = AddressForm()

#     context = {
#         'formAddress': add,
#     }

#     return render(request, 'app/address.html', context)

class AddressListAPIVIew(ListAPIView):
    queryset = Address.objects.all()
    serializer_class = AddressSerializer

class ProfileModelViewSet(ModelViewSet):
    queryset = Profile.objects.all()
    filter_backends = (SearchFilter)
    search_fields = ('phoneNumber', 'name')
    serializer_class = ProfileSerializer