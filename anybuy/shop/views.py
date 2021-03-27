from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.


def index(request):
    return render(request, 'shop/index.html')


def about(request):
    return HttpResponse("At about page")


def contact(request):
    return HttpResponse("At contact page")


def tracker(request):
    return HttpResponse("At tracker page")


def search(request):
    return HttpResponse("At search page")


def product_view(request):
    return HttpResponse("At product view page")


def checkout(request):
    return HttpResponse("At checkout page")
