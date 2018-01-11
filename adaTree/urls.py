from django.urls import path
from . import views

from django.conf import settings
from django.conf.urls.static import static

app_name = 'adaTree'
urlpatterns = [
    path('', views.index, name="index"),
    #path('', views.IndexView.as_view(), name='index'), #using generic ListView
]
