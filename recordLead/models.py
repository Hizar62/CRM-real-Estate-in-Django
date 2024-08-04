# models.py
from django.db import models

class Lead(models.Model):
    PAYMENT_STATUS_CHOICES = [
        ('paid', 'Paid'),
        ('pending', 'Pending'),
    ]
    
    customer_name = models.CharField(max_length=255)
    property_type = models.CharField(max_length=255)
    property_area = models.CharField(max_length=255)
    property_price = models.DecimalField(max_digits=10, decimal_places=2)
    schedule = models.DateTimeField()
    payment_status = models.CharField(max_length=7, choices=PAYMENT_STATUS_CHOICES, default='pending')
    
    def __str__(self):
        return f'{self.customer_name} - {self.property_type}'
