from django.contrib import admin
from django.urls import path
from .views import get_random_fact, index, get_random_student, get_random_dog, get_random_dog_by_breed, get_random_dog_by_sub_breed

urlpatterns = [
    path('admin/', admin.site.urls),
  path('get-random-fact/', get_random_fact, name='get_random_fact'),
  path('get-random-student/', get_random_student, name='get_random_student'),
  path('get_random_dog/', get_random_dog, name='get_random_dog'),
  path('get_random_dog_by_breed/<str:breed>/', get_random_dog_by_breed, name='get_random_dog_by_breed'),
  path('get_random_dog_by_sub_breed/<str:breed>/<str:sub_breed>/', get_random_dog_by_sub_breed, name='get_random_dog_by_sub_breed'),
  path('', index, name='index'),
]