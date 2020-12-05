"""Defines URL patterns for learning_logs"""

from django.urls import path

from . import views

from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

app_name = 'swift_realtys'
urlpatterns = [
    # Home page
    path('', views.index, name='index'),

    # Show all listings.
    path('listings/', views.listings, name='listings'),

    # Detail page for a single listing.
    path('listing/<int:listing_id>/', views.listing, name='listing'),

    # Page for adding a new listing
    path('new_listing/', views.new_listing, name='new_listing'),

    # Page for editing a listing.
    path('edit_listing/<int:listing_id>/', views.edit_listing, name='edit_listing'),

    # Page for about us info
    path('about_us/', views.about_us, name='about_us'),

    # Sort listings by bedrooms
    path('listings_sortbybeds/', views.listings_sortbybeds, name='listings_sortbybeds'),

    # Sort listings by bathrooms
    path('listings_sortbybaths/', views.listings_sortbybaths, name='listings_sortbybaths'),

    # Page for favorites
    path('favorites/', views.favorites, name='favorites'),

    # Add as favorite
    path('favorite/<int:listing_id>/', views.favorite, name='favorite'),

    # Remove Favorite
    path('remove_favorite/<int:listing_id>/', views.remove_favorite, name='remove_favorite'),

    # Page for resources
    path('resources/', views.resources, name='resources'),

    # Show all realtors.
    path('realtors/', views.realtors, name='realtors'),

    # Page for adding a realtor
    path('new_realtor/', views.new_realtor, name='new_realtor'),

    # Page for contact
    path('contact/',views.contact,name="contact"),

]  + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
