from django.urls import path
from helpapp import views

urlpatterns = [
    path('', views.index)
]