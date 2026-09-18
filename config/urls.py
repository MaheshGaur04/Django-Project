from django.urls import include, path
from django.http import HttpResponse


def home(request):
    return HttpResponse('Welcome to my Django API')


urlpatterns = [
    path('', home),
    path('api/', include('products.urls')),
]
