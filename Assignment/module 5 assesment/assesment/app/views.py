from rest_framework import viewsets, filters
from django.db import transaction
from .models import Doctor
from .serializers import DoctorSerializer

class DoctorViewSet(viewsets.ModelViewSet):
    """
    A viewset that provides default `create()`, `retrieve()`, `update()`,
    `partial_update()`, `destroy()` and `list()` actions for Doctor.
    """
    queryset = Doctor.objects.all()
    serializer_class = DoctorSerializer
    
    # Enable filtering by ordering
    filter_backends = [filters.OrderingFilter]
    # Allow ordering by name and specialization fields
    ordering_fields = ['name', 'specialization']
    # Optional: Default ordering
    ordering = ['id']

    @transaction.atomic
    def perform_create(self, serializer):
        """
        Save a new Doctor instance using a database transaction 
        to ensure atomicity. If any error occurs during save, 
        the transaction is rolled back.
        """
        serializer.save()

    @transaction.atomic
    def perform_update(self, serializer):
        """
        Update an existing Doctor instance using a database transaction.
        """
        serializer.save()
