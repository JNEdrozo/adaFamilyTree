from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.template import loader

from django.shortcuts import render
from django.http import Http404

from django.shortcuts import get_object_or_404, render

def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")
