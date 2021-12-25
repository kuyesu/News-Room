from django.urls import path
from blog import views

urlpatterns = [
    path('postdata', views.post_views, name="postdata")
    
]
