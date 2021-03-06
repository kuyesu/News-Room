
from django.shortcuts import render
from newsapi import NewsApiClient
from django.template.loader import render_to_string

from django import template
# Create an object of Library()
register = template.Library()

# Create your views here.

api_key = "382f52e1899e4369bcb6699346f62177"

def bbc(request):
    api_key = "382f52e1899e4369bcb6699346f62177"
    newsapi = NewsApiClient(api_key)
    topheadlines = newsapi.get_top_headlines(sources='bbc-news')


    articles = topheadlines['articles']

    desc = []
    news = []
    img = []

    for i in range(len(articles)):
        myarticles = articles[i]

        news.append(myarticles['title'])
        desc.append(myarticles['description'])
        img.append(myarticles['urlToImage'])


    mylist = zip(news, desc, img)


    return render(request, 'news/bbc.html', context={"mylist":mylist})


@register.inclusion_tag('news/ajazeera.html', takes_context=True)
def aljazeera(request):
    newsapi = NewsApiClient(api_key)
    topheadlines = newsapi.get_top_headlines(sources='al-jazeera-english')


    articles = topheadlines['articles']

    desc = []
    news = []
    img = []

    for i in range(len(articles)):
        myarticles = articles[i]

        news.append(myarticles['title'])
        desc.append(myarticles['description'])
        img.append(myarticles['urlToImage'])


    mylist = zip(news, desc, img)


    return render(request, 'news/ajazeera.html', context={"mylist":mylist})
