from django.shortcuts import render
from django.contrib.auth.decorators import login_required
# Create your views here.
from django.views import generic
from blog.models import *


class ArticlesList(generic.ListView):
    model = Articles
    queryset = Articles.objects.filter(status="Published").order_by('-created_time')
    context_object_name = 'Articles_list'
    template_name = "home/home.html"

class ArticlesDetail(generic.DetailView):
    model = Articles
    template_name = "home/Articles_detail.html"