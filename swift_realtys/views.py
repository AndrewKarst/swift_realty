from django.shortcuts import render
from django.http import HttpResponseRedirect, Http404
from django.urls import reverse
from django.contrib.auth.decorators import login_required

from .models import Listing
from .forms import ListingForm

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
def listings(request):
    """Show all listings"""
    listings = Listing.objects.filter(owner=request.user).order_by('date_added')
    context = {'listings': listings}
    return render(request, 'swift_realtys/listings.html', context)

@login_required
def listing(request, listing_id):
    """Show a single listing"""
    listing = Listing.objects.get(id=listing_id)
    # Make sure the topic belongs to the current user.
    if listing.owner != request.user:
        raise Http404

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
        raise Http404

    if request.method != 'POST':
        # Initial request; pre-fill form with the current entry.
        form = ListingForm(instance=listing_id)
    else:
        # POST data submittedl process data.
        form = ListingForm(instance=listing_id, data=request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('swift_realtys:listing', args=[listing.id]))
    
    context = {'listing': listing, 'form': form}
    return render(request, 'swift_realtys/edit_listing.html', context)

@login_required
def favorites(request):
    """Show favorite listings"""
    listings = Listing.objects.filter(owner=request.user).order_by('date_added')
    context = {'listings': listings}
    return render(request, 'swift_realtys/favorites.html', context)

@login_required
def realtors(request):
    """Show realtors"""
    realtors = Listing.objects.filter(owner=request.user).order_by('date_added')
    context = {'realtors': realtors}
    return render(request, 'swift_realtys/realtors.html', context)
