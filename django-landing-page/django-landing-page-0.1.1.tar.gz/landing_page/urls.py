from django.urls import path

app_name = 'landing-page'

from . import views

urlpatterns = [
    path('<str:slug>', views.by_slug, name='by-slug'),
    path('', views.default, name='default'),
]
