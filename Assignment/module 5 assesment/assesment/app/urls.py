from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import DoctorViewSet

# Create a DefaultRouter instance
router = DefaultRouter()

# Register the DoctorViewSet with the router
# This automatically generates routes for all CRUD operations
# (list, create, retrieve, update, partial_update, destroy)
router.register(r'doctors', DoctorViewSet, basename='doctor')

# Include the router's URLs in the urlpatterns
urlpatterns = [
    path('', include(router.urls)),
]
