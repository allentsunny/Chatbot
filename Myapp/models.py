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
        # choices=SPECIALIZATION_CHOICES,
        default='Other'
    )
    date = models.DateField()
    contact_number = models.CharField(max_length=15)
    email = models.EmailField()
    
    def __str__(self):
        return f"{self.specialization} appointment on {self.date}"
