from rest_framework import generics, status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Course, Student
from .serializers import CourseSerializer, StudentSerializer


class CourseView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        data = CourseSerializer(Course.objects.all(), many=True)
        return Response(data.data)

    def post(self, request):
        data = CourseSerializer(data=request.data)
        if data.is_valid():
            data.save()
            return Response(data.data, status=status.HTTP_201_CREATED)
        return Response(data.errors, status=status.HTTP_400_BAD_REQUEST)


class StudentView(generics.ListCreateAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    permission_classes = [IsAuthenticated]
