from django.db import models

from django.db import models

class Appointment(models.Model):
    SPECIALIZATION_CHOICES = [
        ('Cardiology', 'Cardiology'),
        ('Dermatology', 'Dermatology'),
        ('Orthopedics', 'Orthopedics'),
        ('Pediatrics', 'Pediatrics'),
        ('Other', 'Other'),
    ]
    
    specialization = models.CharField(
        max_length=50,
        choices=SPECIALIZATION_CHOICES,
        default='Other'
    )
    date = models.DateField()
    contact_number = models.CharField(max_length=15)
    email = models.EmailField()
    
    def __str__(self):
        return f"{self.specialization} appointment on {self.date}"


# models.py
# models.py

from django.db import models

class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    subject = models.CharField(max_length=200)
    message = models.TextField()
   

    def __str__(self):
        return f"{self.name} - {self.subject}"
