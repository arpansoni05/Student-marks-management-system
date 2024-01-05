from django.urls import path
from . import views
urlpatterns = [
    path("", views.home, name='home'),
    path("col/", views.college1, name = 'college'),
    
]
