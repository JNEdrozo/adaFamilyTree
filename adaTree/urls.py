from django.urls import dotenv_path

from . import views

app_name = 'adaTree'
urlpatterns = [
    path('', views.index, name="index"),
]
