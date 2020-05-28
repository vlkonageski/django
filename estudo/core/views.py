from django.shortcuts import render, HttpResponse

# Create your views here.


def Hello(request):
    return HttpResponse('<h1>Hello Wolrd</h1>')