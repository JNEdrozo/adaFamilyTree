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
from .models import Instructor
from .models import InternshipCompany
from .models import CapstoneTech

from django.core import serializers
import json

from django.contrib.auth.decorators import login_required

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
@login_required
def index(request):

    template = loader.get_template('adaTree/index.html')

    profiles = OptInProfile.objects.all()
    cohorts = Cohort.objects.all()

    nodes = [{"id": "Ada Developers Academy", "full_name": "Ada Developers Academy", "type": 'program',}]
    #nodes = []
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
            "value": 3,
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


@login_required
def adaTree(request):

    template = loader.get_template('adaTree/adaTree.html')

    profiles = OptInProfile.objects.all()
    cohorts = Cohort.objects.all()
    instructors = Instructor.objects.all()

    nodes = [{"id": "Ada Developers Academy", "full_name": "Ada Developers Academy", "type": 'program'}]
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

    # Instructor Cohort Nodes
    for i in instructors:
        nodes.append({
            # "id": i.pk,
            "id": i.first_name + ' ' + i.last_name,
            "full_name": i.first_name + ' ' + i.last_name,
            "description": i.description,
            "pronouns": i.pronouns,
            "cohorts_served": i.cohorts_served,
            "type": 'staff',
        })

        # Instructor Cohort Links
        instructors_cohort_list = i.cohorts.all()
        for c in instructors_cohort_list:
            links.append({
                "source": i.first_name + ' ' + i.last_name,
                "target": c.cohort_name,
                "value": 2
            })

    data = {
     "nodes": nodes,
     "links": links
    }

    context = {
        'json': json.dumps(data)
    }

    return render(request, 'adaTree/adaTree.html', context)


@login_required
def staffTree(request):
    template = loader.get_template('adaTree/staffTree.html')

    cohorts = Cohort.objects.all()
    instructors = Instructor.objects.all()

    nodes = [{"id": "Ada Developers Academy", "full_name": "Ada Developers Academy", "type": 'program'}]
    links = []

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
            "value": 3,
        })

    # Instructor Cohort Nodes
    for i in instructors:
        nodes.append({
            # "id": i.pk,
            "id": i.first_name + ' ' + i.last_name,
            "full_name": i.first_name + ' ' + i.last_name,
            "description": i.description,
            "pronouns": i.pronouns,
            "cohorts_served": i.cohorts_served,
            "type": 'staff',
        })

        # Instructor Cohort Links
        instructors_cohort_list = i.cohorts.all()
        for c in instructors_cohort_list:
            links.append({
                "source": i.first_name + ' ' + i.last_name,
                "target": c.cohort_name,
                "value": 2
            })

    data = {
      # "nodes": serialized_nodes,
      "nodes": nodes,
      "links": links
    }

    context = {
        'json': json.dumps(data)
    }

    return render(request, 'adaTree/staffTree.html', context)


@login_required
def internships(request):
    template = loader.get_template('adaTree/internships.html')

    profiles = OptInProfile.objects.all()
    companies = InternshipCompany.objects.all()

    nodes = [{"id": "Ada Developers Academy", "full_name": "Ada Developers Academy", "type": 'program'}]
    links = []

    for company in companies:
        if company.name != "Not Applicable":
            # Comany Node data for D3
            nodes.append({
                "id": company.name,
                "full_name": company.name,
                "department": company.department,
                "type": 'company',
            })
            # Company to Ada Links
            links.append({
                "source": company.name,
                "target": "Ada Developers Academy",
                "value": 2.5,
            })


    for profile in profiles:
        if profile.internship_company.name != "Not Applicable":
            # Profile Node data for D3
            nodes.append({
                "id": profile.pk,
                "program": profile.program,
                "full_name": profile.first_name + ' ' + profile.last_name,
                "relation": profile.ada_relation,
                "pronouns": profile.pronouns,
                "cohort": profile.cohort_served,
                "internship": profile.internship_company.name,
                "internship_details": profile.internship_placement,
                "linkedin": profile.linkedin,
                "capstone": profile.capstone_info,
                "type": 'student',
            })
            # Profile to Company Links
            links.append({
                "source": profile.pk,
                "target": profile.internship_company.name,
                "value": 1.5,
            })

    data = {
        "nodes": nodes,
        "links": links
    }

    context = {
        'json': json.dumps(data)
    }

    return render(request, 'adaTree/internships.html', context)


@login_required
def capstoneTech(request):
    template = loader.get_template('adaTree/capstoneTech.html')

    profiles = OptInProfile.objects.all()
    techs = CapstoneTech.objects.all()

    nodes = [{"id": "Ada Developers Academy", "full_name": "Ada Developers Academy", "type": 'program'}]
    links = []

    # Tech Nodes & Links
    for tech in techs:
        nodes.append({
            "id": tech.name,
            "full_name": tech.name,
            "type": 'tech',
        })
        links.append({
            "source": tech.name,
            "target": "Ada Developers Academy",
            "value": .5,
        })

    # Profile Nodes
    for profile in profiles:
        if profile.capstone_tech.count() > 0:
            # Profile Node data for D3
            nodes.append({
                "id": profile.pk,
                "program": profile.program,
                "full_name": profile.first_name + ' ' + profile.last_name,
                "relation": profile.ada_relation,
                "pronouns": profile.pronouns,
                "cohort": profile.cohort_served,
                "internship": profile.internship_company.name,
                "linkedin": profile.linkedin,
                "capstone": profile.capstone_info,
                "type": 'student',
            })

            capstone_techs = profile.capstone_tech.all()
            # print(capstone_techs)
            for tech in capstone_techs:
                # print(str(profile.pk) + ' | ' + str(ct.pk) + ' - ' + ct.name)

                # Profile to Tech Links
                links.append({
                    "source": profile.pk,
                    "target": tech.name,
                    "value": 1.5,
                })

    data = {
     # "nodes": serialized_nodes,
     "nodes": nodes,
     "links": links
    }

    context = {
        'json': json.dumps(data)
    }

    return render(request, 'adaTree/capstoneTech.html', context)
