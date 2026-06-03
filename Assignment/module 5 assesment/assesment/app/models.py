from django.db import models

# Create your models here.

class Doctor(models.Model):
    """
    Doctor model to store doctor details.
    The 'id' field is automatically added by Django as the primary key.
    """
    name = models.CharField(max_length=100, help_text="Full name of the doctor")
    specialization = models.CharField(max_length=100, help_text="Medical specialization (e.g., Cardiologist, Dentist)")
    experience = models.IntegerField(help_text="Years of experience")
    phone = models.CharField(max_length=15, help_text="Contact phone number")
    email = models.EmailField(unique=True, help_text="Unique email address for contact")

    def __str__(self):
        return f"{self.name} - {self.specialization}"
