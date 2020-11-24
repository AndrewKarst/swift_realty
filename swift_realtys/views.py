from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.db import models
from django.contrib.auth.models import User

from .forms import *

from .models import Listing, Realtor
from .forms import ListingForm, RealtorForm
from django.contrib import messages

# Create your views here.

def index(request):
    """The home page for Swift Realty"""
    return render(request, 'swift_realtys/index.html')

def about_us(request):
    """The about us page for Swift Realty"""
    return render(request, 'swift_realtys/about_us.html')

def resources(request):
    """The resources page for Swift Realty"""
    return render(request, 'swift_realtys/resources.html')

@login_required
def listings_sortbybeds(request):
    listings = Listing.objects.all().order_by('-num_bedrooms')
    context = {'listings': listings}
    return render(request, 'swift_realtys/listings.html', context)

@login_required
def listings_sortbybaths(request):
    listings = Listing.objects.all().order_by('-num_bathrooms')
    context = {'listings': listings}
    return render(request, 'swift_realtys/listings.html', context)

@login_required
def listings(request):
    """Show all listings"""
    listings = Listing.objects.all().order_by('date_added')
    context = {'listings': listings}
    return render(request, 'swift_realtys/listings.html', context)


def listing(request, listing_id):
    """Show a single listing"""
    listing = Listing.objects.get(id=listing_id)

    context = {'listing': listing}
    return render(request, 'swift_realtys/listing.html', context)

@login_required
def new_listing(request):
    """Add a new listing."""
    if request.method != 'POST':
        # No data submitted; create a blank form.
        form = ListingForm()
    else:
        # POST data submitted; process data.
        form = ListingForm(request.POST)
        if form.is_valid():
            new_listing = form.save(commit=False)
            new_listing.owner = request.user
            new_listing.save()
            return HttpResponseRedirect(reverse('swift_realtys:listings'))

    context = {'form': form}
    return render(request, 'swift_realtys/new_listing.html', context)

@login_required
def edit_listing(request, listing_id):
    """Edit an existing listing"""
    listing = Listing.objects.get(id=listing_id)
    if listing.owner != request.user:
        raise Http404("You are not the owner and cannot edit this listing.")

    elif request.method != 'POST':
        # Initial request; pre-fill form with the current entry.
        form = ListingForm(instance=listing)
    else:
        # POST data submittedl process data.
        form = ListingForm(instance=listing, data=request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('swift_realtys:listing', args=[listing.id]))

    context = {'listing': listing, 'form': form}
    return render(request, 'swift_realtys/edit_listing.html', context)

@login_required
def favorites(request):
    """Show favorite listings"""
    user = request.user
    listings = user.favorite.all().order_by('date_added')
    context = {'listings': listings}
    return render(request, 'swift_realtys/favorites.html', context)

@login_required
def favorite(request, listing_id):
    user = request.user
    listing = Listing.objects.get(id=listing_id)
    user.favorite.add(listing)
    listings = Listing.objects.all().order_by('date_added')
    context = {'listings': listings}
    return render(request, 'swift_realtys/listings.html', context)

@login_required
def remove_favorite(request, listing_id):
    user = request.user
    listing = Listing.objects.get(id=listing_id)
    user.favorite.remove(listing)
    listings = Listing.objects.all().order_by('date_added')
    context = {'listings': listings}
    return render(request, 'swift_realtys/listings.html', context)

@login_required
def realtors(request):
    """Show realtors"""
    realtors = Realtor.objects.all().order_by('date_added')

    context = {'realtors': realtors}
    return render(request, 'swift_realtys/realtors.html', context)

@login_required
def new_realtor(request):
    """Add a new listing."""
    if request.method != 'POST':
        # No data submitted; create a blank form.
        form = RealtorForm()
    else:
        # POST data submitted; process data.
        form = RealtorForm(request.POST)
        if form.is_valid():
            new_realtor = form.save(commit=False)
            new_realtor.owner = request.user
            new_realtor.save()
            return HttpResponseRedirect(reverse('swift_realtys:realtors'))

    context = {'form': form}
    return render(request, 'swift_realtys/new_realtor.html', context)
