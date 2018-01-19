from django.contrib import admin

# Register your models here.
from .models import Cohort
from .models import OptInProfile
from .models import Instructor
from .models import InternshipCompany
from .models import CapstoneTech

#from .models import Profile
#admin.site.register(Profile)

class OptInProfileAdmin(admin.ModelAdmin):
    search_fields = ('first_name', 'last_name', 'id', 'cohort_served',)
    list_display = ('first_name', 'last_name', 'id', 'cohort_served',)

class CohortAdmin(admin.ModelAdmin):
    search_fields = ('cohort_name',)
    list_display = ('cohort_name', 'grad_year',)

class InstructorAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'id', 'pronouns', 'cohorts_served', 'description',)
    ordering = ('-id',)
    search_fields = ('first_name', 'last_name', 'id',)

class InternshipCompanyAdmin(admin.ModelAdmin):
    list_display = ('name', 'id',)

class CapstoneTechAdmin(admin.ModelAdmin):
    list_display = ('name', 'id',)
    ordering = ('name',)
    search_fields = ('name',)

admin.site.register(Cohort, CohortAdmin)

admin.site.register(OptInProfile, OptInProfileAdmin)

admin.site.register(Instructor, InstructorAdmin)

admin.site.register(InternshipCompany, InternshipCompanyAdmin)

admin.site.register(CapstoneTech, CapstoneTechAdmin)
