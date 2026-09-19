from rest_framework import serializers

from .models import Student


class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = ['id', 'name', 'age', 'course']

    def validate_name(self, value):
        if not value.strip():
            raise serializers.ValidationError('Please enter a name.')
        return value.strip()

    def validate_age(self, value):
        if value < 5 or value > 100:
            raise serializers.ValidationError('Age must be between 5 and 100.')
        return value
