from django.shortcuts import render
from .models import News_post
from .forms import NewsForm


# Create your views here.
def home(request):
    news = News_post.objects.all()
    return render(request, 'news/news.html', {'news': news})

def news_add(request):
    errors = ""
    if request.method == "POST":
        form = NewsForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'news/news.html')
        else:
            errors = "Данные заполнены неверно"
    form = NewsForm()
    return render(request, 'news/news_add.html', {'form': form, 'errors': errors})