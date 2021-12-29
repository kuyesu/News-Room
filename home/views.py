from django.shortcuts import render
from django.contrib.auth.decorators import login_required
# Create your views here.
from django.utils import timezone
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic import FormView
from django.views.generic.edit import CreateView
from django.views.generic.detail import SingleObjectMixin
from django.views import View
from django.views.generic.base import TemplateView

from django.urls import reverse
from django.views import generic
from blog.models import *
from comments.forms import CommentForm 
from comments.models import Comment 
from django.urls import reverse_lazy
from sitesettings.models import *
from newsapi import NewsApiClient


# def home(request):
#     return render(request, 'home/home.html')



class WhatIsNewView(ListView):
    model = WhatIsNew
    template_name = 'home/home.html'
    context_object_name = 'data'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['now'] = timezone.now()
        return context
    def get_queryset(self):
        return WhatIsNew.objects.filter(status="Published").order_by('-created_time')
class ArticleListView(ListView):
    model = Articles
    template_name = 'home/home.html'
    context_object_name = 'posts'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['now'] = timezone.now()
        return context

    def get_queryset(self):
        # Articles.objects.get(slug=self.kwargs['slug'])
        return Articles.objects.filter(status="Published").order_by('-created_time')

    # def get_absolute_url(self):
    #     return reverse('article-detail', args=[str(self.pk)])

class TrendingArticleListView(ListView):
    model = TrendingArticle
    template_name = 'home/home.html'
    context_object_name = 'trending' 
    def get_context_data(self, **kwargs):
        context = super().get_context_dat(**kwargs)
        context['now'] = timezone.now()
        return context
   

  

class ArticleDisplay(DetailView):
    model = Articles
    template_name = "home/articles_detail.html"
    context_object_name = "detail"
    # slug_url_kwarg = "not_slug" # this attribute


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['now'] = timezone.now()
        context['form'] = CommentForm()
        return context

    def get_absolute_url(self):
        return reverse('article-detail', args=[str(self.pk)])

    # def get_context_data(self, **kwargs):
    #     context = super(ArticlesDetail, self).get_context_data(**kwargs)
    #     context['category_list'] = Category.objects.all()
    #     context['source_list'] = Source.objects.all()
    #     return context
    

class CommentFormView(SingleObjectMixin, FormView):
    model = Comment
    template_name = "home/articles_detail.html"
    form_class = CommentForm
    slug_url_kwarg = "not_slug" # this attribute

    def get_queryset(self):
        print(self.kwargs['slug'])
        a = Comment.objects.get(slug=self.kwargs['slug'])
        # print Details.object.get()
        # print Detail.objects.filter(article__slug=self.kwargs['slug']) fails with same error
        return Articles.objects.filter(article=a)

    # def get_object(self, queryset=None):
    #     slug = self.kwargs['slug']
    #     a_obj = Articles.objects.get(slug=slug)
      
    #     d_obj = Comment.objects.get(article=a_obj)
        

    # success_url = reverse_lazy('article-detail')
    
    # def form_valid(self, form):
    #     form.save()
    #     return super().form_valid(form)

    

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        return super().post(request, *args, **kwargs)

    def get_form_kwargs(self):
        kwargs = super(CommentForm, self).get_form_kwargs()
        kwargs['request'] = self.request
        return kwargs

    def form_valid(self, form):
        comment = form.save(commit=False)
        comment.post = self.object
        comment.save()
        return super().form_valid(form)

    def get_success_url(self):
        post = self.get_object()
        return reverse('article-detail', kwargs={'pk': post.pk}) + '#comments'
    
    # def get_absolute_url(self):
    #     return reverse('article-detail', args=[str(self.pk)])

class ArticleDetailView(View):

    def get(self, request, *args, **kwargs):
        view = ArticleDisplay.as_view()
        return view(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        view = CommentFormView.as_view()
        return view(request, *args, **kwargs)

    # def get_absolute_url(self):
    #     return reverse('article-detail', kwargs={"pk": self.pk})


# class HomeView(View):

#     def get(self, request, *args, **kwargs):
#         view = ArticleListView.as_view()
#         view1 = WhatIsNewView.as_view()
        
#         return view1(request, *args, **kwargs) and view(request, *args, **kwargs)

class HomeView(TemplateView):
    template_name = 'home/home.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['posts'] = Articles.objects.filter(status="Published").order_by('-created_time')
        context['data'] = WhatIsNew.objects.filter(status="Published").order_by('-created_time')[:6]
        context['trending_top'] = TrendingArticle.objects.filter(status_choice="Top").order_by('-created_at')[:1]
        context['trending'] = TrendingArticle.objects.filter(status_choice="List").order_by('-created_at')[:3]
        context['category'] = Articles.objects.order_by('-created_time')[:6]
        context['weekly'] = WeeklyArticle.objects.order_by('-created_at')
        context['recent'] = RecentArticle.objects.order_by('-created_at')
        context['adbanner'] = AdvertisementBanner.objects.filter(where_to_locate='Top Banner').order_by('-created_at')[:1]
        context['sitelogo'] = LogoImage.objects.all()[:1]
        context['sidead'] = AdvertisementBanner.objects.filter(where_to_locate='On side').order_by('-created_at')[:1]
        
        context['links'] = Link.objects.all()
        return context




