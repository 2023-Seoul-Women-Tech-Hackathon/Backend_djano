from django.urls import path
from . import views

urlpatterns = [
    path('find_shelters/', views.find_shelters_api, name='find_shelters_api'),
]