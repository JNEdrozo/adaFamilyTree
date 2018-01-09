from django.contrib import admin

# Register your models here.
from .models import Cohort
from .models import Profile

admin.site.register(Cohort)

admin.site.register(Profile)
