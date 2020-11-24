from django import forms

from .models import Listing, Realtor

class ListingForm(forms.ModelForm):
    class Meta:
        model = Listing
        fields = ['address', 'num_bedrooms', 'num_bathrooms', 'description']
        labels = {'address': 'Address:', 'num_bedrooms': 'Bedrooms:', 'num_bathrooms': 'Bathrooms:', 'description': 'Description:'}

class RealtorForm(forms.ModelForm):
    class Meta:
        model = Realtor
        fields = ['name', 'phone_number', 'email_address', 'agency']
        labels = {'name': 'Name:', 'phone_number': 'Phone Number:', 'email_address': 'Email:', 'agancy': 'Agency:' }
