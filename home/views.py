from django.http import HttpResponse
from django.shortcuts import render

from home.models import Settings
from news.models import News


def index(request):
    setting = Settings.objects.get(pk=1)
    sliderdata = News.objects.all()[:4]
    context = {'setting': setting,
               'page': 'home',
               'sliderdata': sliderdata}
    return render(request, 'index.html', context)



