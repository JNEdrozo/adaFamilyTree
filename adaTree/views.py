from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.template import loader

from django.http import Http404

from django.shortcuts import get_object_or_404, render

from .models import OptInProfile


def index(request):
    #return HttpResponse("Hello, world. You're at the adaTree index.")
    template = loader.get_template('adaTree/index.html')
    profiles = OptInProfile.objects.all()
    context = {
        'profiles': profiles
    }

    return render(request, 'adaTree/index.html', context)
