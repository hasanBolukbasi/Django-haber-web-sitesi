from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    text = "Haber Sitesi"
    return HttpResponse("Anasayfa %s." % text)
