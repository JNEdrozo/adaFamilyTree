from django.contrib import admin

# Register your models here.
from .models import Cohort
from .models import OptInProfile

#from .models import Profile
#admin.site.register(Profile)

class OptInProfileAdmin(admin.ModelAdmin):
    search_fields = ('first_name', 'last_name', 'id', 'cohort_served',)
    list_display = ('first_name', 'last_name', 'id', 'cohort_served',)

class CohortAdmin(admin.ModelAdmin):
    search_fields = ('cohort_name',)
    list_display = ('cohort_name',)
admin.site.register(Cohort, CohortAdmin)

admin.site.register(OptInProfile, OptInProfileAdmin)
