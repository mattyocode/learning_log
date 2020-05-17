'''Defines URL patterns for learning_logs.'''

from django.urls import path, include

from . import views

app_name = 'learning_logs'
urlpatterns = [
    #Homepage
    path('', views.index, name='index'),
]