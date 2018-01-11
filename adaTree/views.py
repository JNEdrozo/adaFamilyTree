from django.shortcuts import get_object_or_404, render

from django.http import HttpResponse
from django.template import loader
from django.http import Http404

# from django.http import HttpResponseRedirect
# from django.urls import reverse
from django.views import generic
from django.views.generic import TemplateView

from .models import OptInProfile

from django.core import serializers
import json

# CREATE VIEWS HERE---------------------------------------

# GENERIC CLASS INDEX VIEW
# class IndexView(generic.ListView):
#     template_name = 'adaTree/index.html'
#
#     def get_queryset(self):
#         return OptInProfile.objects.all()

# GENERAL INDEX VIEW (to list all profile names)
# def index(request):
#
#     template = loader.get_template('adaTree/index.html')
#     profiles = OptInProfile.objects.all()
#     context = {
#         'profiles': profiles
#     }
#
#     return render(request, 'adaTree/index.html', context)

# INDEX VIEW (with json data passed to template)
def index(request):

    template = loader.get_template('adaTree/index.html')

    nodes = OptInProfile.objects.all()
    links = []

    for node in nodes:
        links.append({"source": node.pk, "target": node.cohort_served, "value": 1})

    serialized_nodes = serializers.serialize('json', nodes)
    # serialized_links = serializers.serialize('json', links)

    data = {
     "nodes": serialized_nodes,
     "links": links
    }

    # profiles = OptInProfile.objects.only("ada_relation", "capstone_info", "cohort_served", "first_name", "internship_placement", "last_name", "linkedin", "program", "pronouns")
    # serialized_context = serializers.serialize('json', json)
    # serialized_links = serializers.serialize('json', links)

    # context = {
    #     'nodes': serialized_nodes,
    #     'links': links
    # }

    context = {
        'json': json.dumps(data)
    }

    return render(request, 'adaTree/index.html', context)
