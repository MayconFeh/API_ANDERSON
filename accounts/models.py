from django.db import models
from django.contrib.auth.models import AbstractUser
from uuid import uuid4

USERTYPE_CHOICES = (('USR', 'User'), ('ADM', 'Admin'))


class Account(AbstractUser):
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    userType = models.CharField(max_length=3, choices=USERTYPE_CHOICES, default=USERTYPE_CHOICES[0])
    name = models.CharField(max_length=50)
    username = models.CharField(max_length=50, unique=True)
    email = models.EmailField(max_length=100, unique=True)
    password = models.CharField(max_length=200)
    phone = models.CharField(max_length=16, blank=True)
    cpf_or_cnpj = models.CharField(max_length=45, unique=True)
    photo = models.ImageField(upload_to='user_photos', blank=True, null=True)
    address = models.CharField(max_length=60, blank=True)
    address_number = models.CharField(max_length=10, blank=True)
    address_complement = models.CharField(max_length=120, blank=True)
    city = models.CharField(max_length=60, blank=True)
    state = models.CharField(max_length=60, blank=True)
    zipcode = models.CharField(max_length=10)
    gender = models.CharField(max_length=10, blank=True)
    profileVisibility = models.BooleanField(default=True)
    dateOfBirth = models.DateField(null=True)
    bio = models.TextField(null=True)
    facebook = models.CharField(max_length=100, null=True)
    twitter = models.CharField(max_length=100, null=True)
    instagram = models.CharField(max_length=100, null=True)
