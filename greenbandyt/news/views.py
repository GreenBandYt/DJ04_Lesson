from django.shortcuts import render
from .models import News_post
from .forms import NewsForm


# Create your views here.
def home(request):
    news = News_post.objects.all()
    return render(request, 'news/news.html', {'news': news})

def news_add(request):
    form = NewsForm()
    return render(request, 'news/news_add.html', {'form': form})