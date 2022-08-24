from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return HttpResponse("Hello Doctors App Here")


def edit(request):
    return HttpResponse("Hello Doctors EDIT")
