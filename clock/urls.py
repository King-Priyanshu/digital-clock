from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    
    path('', include('timedate.urls')),  # Include URLs from the clock app
]
