from rest_framework import serializers

from .models import Course, Student


class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = ['id', 'name']

    def validate_name(self, value):
        if not value.strip():
            raise serializers.ValidationError('Please enter a course name.')
        return value.strip()


class StudentSerializer(serializers.ModelSerializer):
    course = CourseSerializer(read_only=True)
    course_id = serializers.PrimaryKeyRelatedField(
        source='course',
        queryset=Course.objects.all(),
        write_only=True,
    )

    class Meta:
        model = Student
        fields = ['id', 'name', 'age', 'course', 'course_id']

    def validate_name(self, value):
        if not value.strip():
            raise serializers.ValidationError('Please enter a name.')
        return value.strip()

    def validate_age(self, value):
        if value < 5 or value > 100:
            raise serializers.ValidationError('Age must be between 5 and 100.')
        return value
