from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(request):
    return render(request, 'menu/home.html')


def test_url(request):
    return HttpResponse("тестовый переход 1 ")


def test_url1(request):
    return HttpResponse("тестовый переход 2")


def test_url2(request):
    return HttpResponse("тестовый переход 3")