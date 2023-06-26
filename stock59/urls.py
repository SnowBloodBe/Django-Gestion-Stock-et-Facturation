from django.contrib import admin
from django.urls import path, include
from pages import views

urlpatterns = [
    path('', admin.site.urls), 
    # path('',include('pages.urls')),

    

    ]

