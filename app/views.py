from django.shortcuts import render,get_object_or_404
from .models import Yangiliklar,Olimpiada,AboutSchool,Leadership,Yonalish,Category
import re

def extract_youtube_id(url):
    """Extracts the YouTube video ID from a given URL."""
    match = re.search(r'(?:v=|\/)([0-9A-Za-z_-]{11})', url)
    return match.group(1) if match else None


def home(request):
    latest_post = Yangiliklar.objects.all().order_by('-date')[:1]
    other_posts = Yangiliklar.objects.all().order_by('-date')[1:5]
    
    about_school = AboutSchool.objects.first()
    category = Category.objects.all()
    return render(request, 'home.html', {'latest_post': latest_post, 'other_posts': other_posts,'about_school':about_school, 'categories':category})

def news_detail(request, pk):
    categories = Category.objects.all()
    new = get_object_or_404(Yangiliklar, pk=pk)
    return render(request, 'detail.html', {'new': new,'categories': categories})

def devon(request):
    categories = Category.objects.all()
    return render(request, 'devon.html', {'categories': categories})

def leadership(request):
    categories = Category.objects.all()
    a = Leadership.objects.first()
    return render(request, 'leadership.html', {'a': a,'categories':categories})

def news(request):
    categories = Category.objects.all()
    news_list = Yangiliklar.objects.all().order_by('-date')
    return render(request, 'news.html', {'news_list': news_list,'categories': categories})

def olimpiada(request):
    categories = Category.objects.all()
    olimpiada = Olimpiada.objects.all()
    return render(request, 'olimpiada.html', {'olimpiada': olimpiada,'categories': categories})

def yunalish_list(request, pk):
    categories = Category.objects.all()
    category = get_object_or_404(Category, pk=pk)
    yunalish = Yonalish.objects.filter(yonalish=category)
    return render(request, 'yunalish_list.html', {'yunalish': yunalish, 'category': category,'categories': categories})

def yunalish_detail(request, pk):
    categories = Category.objects.all()
    new = get_object_or_404(Yonalish, pk=pk)
    return render(request, 'detail.html', {'new': new,'categories': categories})