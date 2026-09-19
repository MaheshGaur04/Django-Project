from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import Course, Student
from .serializers import CourseSerializer, StudentSerializer


@api_view(['GET', 'POST'])
def student(req):
    if req.method == 'GET':
        data = StudentSerializer(Student.objects.all(), many=True)
        return Response(data.data)

    data = StudentSerializer(data=req.data)
    if data.is_valid():
        data.save()
        return Response(data.data, status=status.HTTP_201_CREATED)

    return Response(data.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'POST'])
def course(req):
    if req.method == 'GET':
        data = CourseSerializer(Course.objects.all(), many=True)
        return Response(data.data)

    data = CourseSerializer(data=req.data)
    if data.is_valid():
        data.save()
        return Response(data.data, status=status.HTTP_201_CREATED)

    return Response(data.errors, status=status.HTTP_400_BAD_REQUEST)
