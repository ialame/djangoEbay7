from django.urls import path

from magic import views

urlpatterns = [
    path('', views.index, name='index'),
]