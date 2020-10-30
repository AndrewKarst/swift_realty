"""Defines URL patterns for learning_logs"""

from django.urls import path

from . import views

app_name = 'swift_realtys'
urlpatterns = [
    # Home page
    path('', views.index, name='index'),

    # Show all listingss.
    path('listings/', views.listings, name='listings'),

    # Detail page for a single listing.
    path('listing/<int:listing_id>/', views.listing, name='listing'),

    # Page for adding a new listing
    path('new_listing/', views.new_listing, name='new_listing'),

    # Page for editing a listing.
    path('edit_listing/<int:listing_id>/', views.edit_listing, name='edit_listing'),

    # Page for about us info
    path('about_us/', views.about_us, name='about_us'),

    # Page for favorites
    path('favorites/', views.favorites, name='favorites'),
    
    # Page for resources
    path('resources/', views.resources, name='resources'),

    # Show all realtors.
    path('realtors/', views.realtors, name='realtors'),
]