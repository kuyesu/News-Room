from django.urls import path
from home import views

from .views import ArticleListView

urlpatterns = [
    path('', views.HomeView.as_view(), name='home'),
    path('<slug:slug>', views.ArticleDetailView.as_view(), name='article-detail'),
    
]
