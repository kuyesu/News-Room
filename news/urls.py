from django.urls import path
from . import views

urlpatterns = [
    path('bbc/', views.bbc, name = 'BBC'),
]
