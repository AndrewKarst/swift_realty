from django.db import models
from django.contrib.auth.models import User, UserManager


# Create your models here.
class Listing(models.Model):
    """A listing for a home for sale"""
    address = models.CharField(max_length=200, default='none')
    num_bedrooms = models.IntegerField(default=0)
    num_bathrooms = models.IntegerField(default=0)
    description = models.CharField(max_length=200, default='none')
    photo = models.ImageField(upload_to='images', blank=True, null=True)
    date_added = models.DateTimeField(auto_now_add=True)
    text = models.CharField(max_length=200, default='none')
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    favorite = models.ManyToManyField(User, related_name='favorite', default='none', blank=True)

    @property
    def get_photo_url(self):
        if self.photo and hasattr(self.photo, 'url'):
            return self.photo.url
        else:
            return "/media/images/house-placeholder.jpg"

    class Meta:
        verbose_name_plural = 'listings'

class Realtor(models.Model):
    """Information about a realtor"""
    name = models.CharField(max_length=200, default='none')
    phone_number = models.CharField(max_length=200, default='none')
    email_address = models.EmailField(default='none')
    agency = models.CharField(max_length=200, default='none')
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    date_added = models.DateTimeField(auto_now_add=True)
    photo = models.ImageField(upload_to='realtor_photo', blank=True, null=True)

    @property
    def get_photo_url(self):
        if self.photo and hasattr(self.photo, 'url'):
            return self.photo.url
        else:
            return "/media/realtor_photo/realtor-placeholder.jpg"

    class Meta:
        verbose_name_plural = 'realtors'
