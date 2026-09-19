from django.urls import path

from .views import CourseView, StudentView

urlpatterns = [
    path('students/', StudentView.as_view()),
    path('courses/', CourseView.as_view()),
]
