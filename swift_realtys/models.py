from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Listing(models.Model):
    """A listing for a home for sale"""
    address = models.CharField(max_length=200, default='none')
    num_bedrooms = models.IntegerField(default=0)
    num_bathrooms = models.IntegerField(default=0)
    description = models.CharField(max_length=200, default='none')
    photo = models.ImageField(upload_to='homes', default='none')
    date_added = models.DateTimeField(auto_now_add=True)
    text = models.CharField(max_length=200, default='none')
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    favorite = models.BooleanField(default=False)