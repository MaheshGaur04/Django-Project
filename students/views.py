from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import Student


@api_view(['GET', 'POST'])
def student(req):
    if req.method == 'GET':
        rows = Student.objects.values('id', 'name', 'age', 'course')
        return Response(list(rows))

    name = req.data.get('name')
    age = req.data.get('age')
    course = req.data.get('course')

    if not name or age is None or not course:
        return Response(
            {'error': 'Please enter the name, age and course.'},
            status=status.HTTP_400_BAD_REQUEST,
        )

    item = Student.objects.create(name=name, age=age, course=course)
    return Response(
        {
            'id': item.id,
            'name': item.name,
            'age': item.age,
            'course': item.course,
        },
        status=status.HTTP_201_CREATED,
    )
