from django.shortcuts import render, redirect
from django.views.generic.list import ListView
from .models import *
from .forms import ArticlesForm
# Create your views here.


def post_views(request):
    if request.method == "POST":
        form = ArticlesForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("postdata")
    else:
        form = ArticlesForm()
        return render(request, 'post/postdata.html', {'form': form})