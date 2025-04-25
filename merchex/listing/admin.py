from django.contrib import admin
from .models import Groupe,Listing

@admin.register(Groupe)
class GroupeAdmin(admin.ModelAdmin):
    list_display = ['nom','genre','year_formed']

@admin.register(Listing)
class ListingAdmin(admin.ModelAdmin):
    list_display = ['title','groupe','sold']