from django.contrib import admin
from django.urls import path

from .views import getShelter

urlpatterns = [
    path('get/', getShelter),
]
