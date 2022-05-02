from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def sermonpage(request):
    return HttpResponse('i win')

def index(request):
    return HttpResponse('i win')
