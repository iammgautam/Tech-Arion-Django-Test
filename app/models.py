from django.db import models
from django.contrib.auth.models import User
# Create your models here.
GENDER = [
    ('Male', 'Male'),
    ('Female', 'Female'),
]

class Profile(models.Model):
    name = models.CharField(max_length=50)
    dateOfBirth = models.DateField()
    gender = models.CharField(choices = GENDER, max_length=10)
    phoneNumber = models.PositiveBigIntegerField()

    def __str__(self):
        return self.name
    # def get_age(self):
    #     age = datetime.date.today()-self.dateOfBirth
    #     return int((age).days/365.25)

class Address(models.Model):
    owner = models.ForeignKey('Profile', on_delete=models.CASCADE, related_name="profile")
    address1 = models.TextField(max_length=300)
    address2 = models.TextField(max_length=300)
    pincode = models.PositiveIntegerField()

    def __str__(self):
        return self.owner