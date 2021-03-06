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
class Program(models.Model):
    name = models.CharField(max_length=100, blank=True)


class Cohort(models.Model):
    cohort_name = models.CharField(max_length=200, blank=False)
    grad_year = models.CharField(max_length=4, blank=False)
    description = models.TextField(max_length=500,blank=True)

    def __str__(self):
        return "%s" % (self.cohort_name)


class CapstoneTech(models.Model):
    name = models.CharField(max_length=100, blank=False)
    description = models.TextField(max_length=500,blank=True)

    def __str__(self):
        return "%s" % (self.name)

    @property
    def tech_students(self):
        tech_students = OptInProfile.objects.filter(capstone_tech__name = self.name).order_by('first_name')
        student_list = []

        for student in tech_students:
            full_name = " %s %s - %s" % (student.first_name, student.last_name, student.cohort_served)
            student_list.append(full_name)

        return student_list


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

    internship_company = models.ForeignKey('InternshipCompany', on_delete=models.CASCADE)

    internship_placement = models.TextField(max_length=500, blank=True)

    linkedin = models.CharField(max_length=200, blank=True)

    capstone_info = models.TextField(max_length=500,blank=True)

    email = models.CharField(max_length=200, blank=True)

    capstone_tech = models.ManyToManyField(CapstoneTech)

    def __str__(self):
        return "%s %s (%s)" % (self.first_name, self.last_name, self.id)
        #return '{}'.format(self.first_name)

    @property
    def capstone_techstack(self):
        return ", ".join([tech.name for tech in self.capstone_tech.all().order_by('name')])


class Instructor(models.Model):
    first_name = models.CharField(max_length=100, blank=False)
    last_name = models.CharField(max_length=100, blank=False)
    email = models.EmailField(max_length=500,blank=True)
    description = models.TextField(max_length=500,blank=True)
    cohorts = models.ManyToManyField(Cohort)
    pronouns = models.CharField(max_length=100, blank=True)

    def __str__(self):
        return "%s %s (%s)" % (self.first_name, self.last_name, self.id)

    @property
    def cohorts_served(self):
        return ", ".join([c.cohort_name for c in self.cohorts.all().order_by('cohort_name')])


class InternshipCompany(models.Model):
    name = models.CharField(max_length=100, blank=False)
    department = models.CharField(max_length=100, blank=True)
    description = models.TextField(max_length=500,blank=True)

    def __str__(self):
        return "%s" % (self.name)

    @property
    def company_students(self):
        company = InternshipCompany.objects.get(pk = self.pk)
        #Note: optinprofile is all lower case for the many-to-one relationship (different from many-to-many where camelcase model letters are separated by underscores)
        student_queryset = company.optinprofile_set.all().order_by('first_name')
        student_list = []

        for student in student_queryset:
            full_name = " %s %s - %s" % (student.first_name, student.last_name, student.cohort_served)
            student_list.append(full_name)

        return student_list


class Staff(models.Model):
    first_name = models.CharField(max_length=100, blank=False)
    last_name = models.CharField(max_length=100, blank=False)
    description = models.CharField(max_length=100, blank=True)
