from rest_framework import serializers
from .models import Doctor

class DoctorSerializer(serializers.ModelSerializer):
    """
    Serializer for the Doctor model.
    Handles converting model instances to JSON and validating incoming data.
    """
    
    class Meta:
        model = Doctor
        fields = ['id', 'name', 'specialization', 'experience', 'phone', 'email']
        
    def validate_name(self, value):
        """
        Check that the doctor's name is at least 3 characters long.
        """
        if len(value) < 3:
            raise serializers.ValidationError("Doctor name must be at least 3 characters long.")
        return value
        
    def validate_experience(self, value):
        """
        Check that experience is not negative.
        """
        if value < 0:
            raise serializers.ValidationError("Experience cannot be negative.")
        return value

    # Email uniqueness is automatically handled by DRF because 'unique=True' 
    # is set on the email field in the Doctor model, but we could add explicit 
    # validation here if we wanted to customize the error message.
