from django.urls import path

from . import views

app_name = 'slaves'

urlpatterns = [
    path('', views.index, name='index'),
]
