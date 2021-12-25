from django.urls import path
from home import views

urlpatterns = [
    path('', views.ArticlesList.as_view(), name='home'),
    path('<slug:slug>/', views.ArticlesDetail.as_view(), name='Articles_detail'),
]
