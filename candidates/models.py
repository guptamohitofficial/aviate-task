from django.db import models
from phonenumber_field.modelfields import PhoneNumberField

class Candidate(models.Model):
    GENDER_CHOICES = (
        ('M', 'Male'),
        ('F', 'Female'),
        ('O', 'Other')
    )

    name = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    age = models.PositiveIntegerField(null=True, blank=True)
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES, null=True, blank=True)
    phone_number = PhoneNumberField(null=True, blank=True)

    def __str__(self):
        return self.name
