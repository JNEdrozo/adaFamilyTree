from django.db import models
from django.contrib.auth.models import User

# # Cohort Information
# C1 = 'C1'
# C2 = 'C2'
# C3 = 'C3'
# C4 = 'C4'
# C5 = 'C5'
# C6_BRACKETS = 'C6 Brackets'
# C6_PARENS = 'C6 Parens'
# C7_QUEUES = 'C7 Queues'
# C7_STACKS = 'C7 Stacks'
# C8_CARETS = 'C8 Carets'
# C8_PIPES = 'C8 Pipes'
#
# COHORT_CLASSES = (
#     (C1, '(Oct 2014)'),
#     (C2, '(Aug 2015)'),
#     (C3, '(April 2016)'),
#     (C4, '(Sept 2016)'),
#     (C5, '(Feb 2017)'),
#     (C6_BRACKETS, '(July 2017)'),
#     (C6_PARENS, '(July 2017)'),
#     (C7_QUEUES, '(Jan 2018)'),
#     (C7_STACKS,'(Jan 2018)'),
#     (C8_CARETS, '(July 2018)'),
#     (C8_PIPES, '(July 2018)'),
# )

# Create your models here.
class Cohort(models.Model):
    cohort_name = models.CharField(max_length=200, blank=False)
    grad_year = models.CharField(max_length=4, blank=False)
    description = models.TextField(max_length=500,blank=True)

    def __str__(self):
        return "%s" % (self.cohort_name)


class Profile(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE) #Use so new users can add their own profiles

    program = models.CharField(max_length=100, blank=False)

    first_name = models.CharField(max_length=100, blank=False)

    last_name = models.CharField(max_length=100, blank=False)

    ada_relation = models.CharField(max_length=100, blank=False)

    pronouns = models.CharField(max_length=100, blank=False)

    #cohort_served = models.ManyToManyField(Cohort) #If staff & students were creating profiles as general non-admin users: https://stackoverflow.com/questions/2726476/django-multiple-choice-field-checkbox-select-multiple/4033308

    cohort_served = models.CharField(max_length=100, blank=False)

    github_username = models.CharField(max_length=100, blank=False)

    internship_placement = models.TextField(max_length=500, blank=True)

    linkedin = models.CharField(max_length=200, blank=True)

    capstone_info = models.TextField(max_length=500,blank=True)

    email = models.CharField(max_length=200, blank=True)


class OptInProfile(models.Model):

    program = models.CharField(max_length=100, blank=False)

    first_name = models.CharField(max_length=100, blank=False)

    last_name = models.CharField(max_length=100, blank=False)

    ada_relation = models.CharField(max_length=100, blank=False)

    pronouns = models.CharField(max_length=100, blank=False)

    cohort_served = models.CharField(max_length=100, blank=False)

    github_username = models.CharField(max_length=100, blank=False)

    internship_placement = models.TextField(max_length=500, blank=True)

    linkedin = models.CharField(max_length=200, blank=True)

    capstone_info = models.TextField(max_length=500,blank=True)

    email = models.CharField(max_length=200, blank=True)


class Instructor(models.Model):
    first_name = models.CharField(max_length=100, blank=False)
    last_name = models.CharField(max_length=100, blank=False)
    email = models.EmailField(max_length=500,blank=True)
    description = models.TextField(max_length=500,blank=True)
    cohorts = models.ManyToManyField(Cohort)
    pronouns = models.CharField(max_length=100, blank=True)

    def __str__(self):
        return "%s %s" % (self.first_name, self.last_name)

    def cohorts_served(self):
        return ", ".join([c.cohort_name for c in self.cohorts.all().order_by('cohort_name')])
