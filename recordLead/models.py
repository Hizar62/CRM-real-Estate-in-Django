from django.db import models

# Create your models here.
class Lead(models.Model):
    customer_name = models.CharField(max_length=50)
    property_type = models.CharField(max_length=40)
    property_area = models.CharField(max_length=40)
    property_price = models.IntegerField()
    schedule = models.DateTimeField()

    