from django.urls import path
from . import views

urlpatterns = [
  path('', views.home, name='home'),
  path('about/', views.about, name='about'),
  # route for puppies index
  path('puppies/', views.puppies_index, name='index'),
]
