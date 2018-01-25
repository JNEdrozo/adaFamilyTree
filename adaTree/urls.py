from django.urls import path
from . import views

from django.conf import settings
from django.conf.urls.static import static

app_name = 'adaTree'
urlpatterns = [
    path('', views.index, name="index"),
    path('students/', views.students, name="students"),
    path('adaTree/', views.adaTree, name="adaTree"),
    path('adaTreeLabel/', views.adaTreeLabel, name="adaTreeLabel"),
    path('staffTree/', views.staffTree, name="staffTree"),
    path('staffTreeLabel/', views.staffTreeLabel, name="staffTreeLabel"),
    path('internships/', views.internships, name="internships"),
    path('internshipsLabel/', views.internshipsLabel, name="internshipsLabel"),
    path('capstoneTech/', views.capstoneTech, name="capstoneTech"),
    path('capstoneTechLabel/', views.capstoneTechLabel, name="capstoneTechLabel"),
    #path('', views.IndexView.as_view(), name='index'), #using generic ListView
]
