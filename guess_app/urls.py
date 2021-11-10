from django.urls import path
from guess_app import views

urlpatterns = [
    path('', views.guess_app, name='guess_app'),
]