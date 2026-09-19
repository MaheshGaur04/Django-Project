from django.urls import path

from .views import course, student

urlpatterns = [
    path('students/', student),
    path('courses/', course),
]
