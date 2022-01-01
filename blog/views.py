from django.shortcuts import render, redirect
from django.views.generic.list import ListView
from django.views.generic.base import TemplateView

from .models import *
from .forms import ArticlesForm
# Create your views here.
from django.contrib.auth.decorators import login_required


from django.contrib import messages
class HomeView(TemplateView):
    template_name = "home.html"

@login_required
def home_view(request):
    return render(request, "home/home.html")

def post_views(request):
    if request.method == "POST":
        form = ArticlesForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("postdata")
    else:
        form = ArticlesForm()
        return render(request, 'post/postdata.html', {'form': form})


def add_article(request):
    return render(request, 'post/add_article.html')

def add_article_save(request):
    if request.method == 'POST':
        messages.error(request, "Invalid Post")
        return redirect('add_article')
    else:
        article = request.POST.get('article')
        try:
            article_model = Articles(post_name=article)
            article_model.save()
            messages.success(request, "Article Added Successfully")
            return redirect('add_article')
        except:
            messages.error(request, "Failed to Add Article")
            return redirect('add_article')

def manage_article(request):
    articles = Articles.objects.all()
    context = {
        'articles' : articles
    }
    return render(request, 'post/manage_articles.html', context)

def edit_article(request, article_id):
    article = Articles.objects.get(id=article_id)
    context = {
        'article' : article,
        'article_id' : article_id
    }
    return render(request, 'post/edit_article.html', context)

def edit_article_save(request):
    