from django.urls import path
from .views  import *

urlpatterns = [
    path('',hello),
    path('about_us/',about_us),
    path('listings/',listings),
    path('contact_us/',contact_us)
]