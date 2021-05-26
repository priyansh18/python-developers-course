from django.db.models.base import Model
from django.http.response import Http404
from django.shortcuts import get_object_or_404, render
from . import models
# Create your views here.


def index(request):
    # Getting first 10 Articles from Articles
    latest_articles = models.Article.objects.all().order_by('-createdAt')[:10]
    # This query won't hit the database unless this variable where it is stored in used somewhere so we can say it as a lazy query
    # print(latest_articles)
    context = {
        'latest_articles': latest_articles
    }
    return render(request, 'main/index.html', context)


def article(request, pk):
    # try:
    #     article = models.Article.objects.get(pk=pk)
    # except:
    #     raise Http404

    article = get_object_or_404(models.Article.objects, pk=pk)

    context = {
        'article': article
    }

    return render(request, 'main/article.html', context)


def author(request, pk):

    author = get_object_or_404(models.Author.objects, pk=pk)

    context = {
        'author': author,
    }

    return render(request, 'main/author.html', context)

def create_article(request):
    print(request.POST)
    authors = models.Author.objects.all()
    context = {
        'authors':authors
    }
    if request.method == 'POST':
        article_data = {
            'title':request.POST['title'],
            'content':request.POST['content'],
        }
        article = models.Article.objects.create(**article_data)
        author = models.Author.objects.get(pk=request.POST['author'])
        article.authors.set([author])
        context['success'] = True
 
    return render(request,'main/create_article.html',context)