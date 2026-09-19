from django.http import HttpResponse
from django.urls import include, path
from rest_framework.authtoken.views import obtain_auth_token
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView


def home(request):
    return HttpResponse('Welcome to my Django API')


urlpatterns = [
    path('', home),
    path('api/', include('students.urls')),
    path('api/token/', obtain_auth_token),
    path('api/jwt/', TokenObtainPairView.as_view()),
    path('api/jwt/refresh/', TokenRefreshView.as_view()),
]
