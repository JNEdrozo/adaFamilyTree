from django.contrib import admin

# Register your models here.
from .models import Cohort
from .models import Profile
from .models import OptInProfile

admin.site.register(Cohort)

admin.site.register(Profile)

admin.site.register(OptInProfile)
