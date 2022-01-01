from django.urls import path
from blog import views

urlpatterns = [
    path('', views.home_view, name='home'),
    path('postdata', views.post_views, name="postdata")
    
]
