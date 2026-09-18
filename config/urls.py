from django.http import HttpResponse
from django.urls import include, path


def home(request):
    return HttpResponse('Welcome to my Django API')


urlpatterns = [
    path('', home),
    path('api/', include('students.urls')),
]
