from django.urls import path
from blog import views

urlpatterns = [
    path('', views.HomeView.as_view(), name='home'),
    path('postdata', views.post_views, name="postdata"),

    # Articles
    path('add_article', views.add_article, name='add_article'),
    path('add_article_save', views.add_article_save, name='add_article_save'),
    path('manage_article', views.manage_article, name='manage_article'),
    path('edit_article/<int:article_id>', views.edit_article, name='edit_article'),
    path('edit_article_save', views.edit_article_save, name='edit_article_save'),
    path('delete_article/<int:article_id>', views.delete_article, name='delete_article'),
    
    
]
