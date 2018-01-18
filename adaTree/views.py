from django.shortcuts import get_object_or_404, render

from django.http import HttpResponse
from django.template import loader
from django.http import Http404

# from django.http import HttpResponseRedirect
# from django.urls import reverse
from django.views import generic
from django.views.generic import TemplateView

from .models import OptInProfile
from .models import Cohort

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

    profiles = OptInProfile.objects.all()
    cohorts = Cohort.objects.all()

    nodes = [{"id": "Ada Developers Academy", "full_name": "Ada Developers Academy"}]
    # nodes = []
    links = []

    for profile in profiles:
        # Node data for D3
        nodes.append({
            "id": profile.pk,
            "program": profile.program,
            "full_name": profile.first_name + ' ' + profile.last_name,
            "relation": profile.ada_relation,
            "pronouns": profile.pronouns,
            "cohort": profile.cohort_served,
            "internship": profile.internship_placement,
            "linkedin": profile.linkedin,
            "capstone": profile.capstone_info,
            "type": 'student',
        })
        # Link data for D3
        links.append({
            "source": profile.pk,
            "target": profile.cohort_served,
            # "target": {"id": profile.cohort_served},
            "value": 2,
        })

    for cohort in cohorts:
        nodes.append({
            "id": cohort.cohort_name,
            "full_name": cohort.cohort_name,
            "cohort": cohort.cohort_name,
            "type": 'cohort',
        })
        links.append({
            "source": cohort.cohort_name,
            "target": "Ada Developers Academy",
            # "target": {"id": profile.cohort_served},
            "value": 4,
        })

    # serialized_nodes = serializers.serialize('json', nodes)
    # serialized_links = serializers.serialize('json', links)

    data = {
     # "nodes": serialized_nodes,
     "nodes": nodes,
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


def adaTree(request):

    template = loader.get_template('adaTree/adaTree.html')

    profiles = OptInProfile.objects.all()
    cohorts = Cohort.objects.all()

    nodes = [{"id": "Ada Developers Academy", "full_name": "Ada Developers Academy"}]
    links = []

    for profile in profiles:
        # Node data for D3
        nodes.append({
            "id": profile.pk,
            "program": profile.program,
            "full_name": profile.first_name + ' ' + profile.last_name,
            "relation": profile.ada_relation,
            "pronouns": profile.pronouns,
            "cohort": profile.cohort_served,
            "internship": profile.internship_placement,
            "linkedin": profile.linkedin,
            "capstone": profile.capstone_info,
            "type": 'student',
        })
        # Link data for D3
        links.append({
            "source": profile.pk,
            "target": profile.cohort_served,
            # "target": {"id": profile.cohort_served},
            "value": 2,
        })

    for cohort in cohorts:
        nodes.append({
            "id": cohort.cohort_name,
            "full_name": cohort.cohort_name,
            "cohort": cohort.cohort_name,
            "type": 'cohort',
        })
        links.append({
            "source": cohort.cohort_name,
            "target": "Ada Developers Academy",
            # "target": {"id": profile.cohort_served},
            "value": 4,
        })

    data = {
     # "nodes": serialized_nodes,
     "nodes": nodes,
     "links": links
    }

    context = {
        'json': json.dumps(data)
    }

    return render(request, 'adaTree/adaTree.html', context)
