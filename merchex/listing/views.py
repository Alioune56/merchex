from django.shortcuts import render
from django.http import HttpResponse

from .models import Groupe,Listing


def hello(request):
    # Afficher toute la liste des groupes
    g = Groupe.objects.all()
    context = {'groupes':g}
    return render(request,'listings/hello.html',context)

def about_us(request):
    return render(request,'listings/about.html')

def listings(request):
    # Afficher les listings
    l = Listing.objects.all()
    context = {'listings':l}
    return render(request,'listings/listing.html',context)

def contact_us(request):
    return render(request,'listings/contact.html')