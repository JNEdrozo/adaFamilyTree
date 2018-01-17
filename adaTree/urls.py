from django.urls import path
from . import views

from django.conf import settings
from django.conf.urls.static import static

from django.conf.urls import url
from django.contrib.auth import views as auth_views

app_name = 'adaTree'
urlpatterns = [
    url(r'^login/$', auth_views.login, name='login'),
    url(r'^logout/$', auth_views.logout, name='logout'),
    path('', views.index, name="index"),
    path('adaTree/', views.adaTree, name="adaTree"),
    #path('', views.IndexView.as_view(), name='index'), #using generic ListView
]
