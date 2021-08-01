from django.db import models

# Create your models here.
class Measurement(models.Model):
    location=models.CharField(max_length=1000)
    destination=models.CharField(max_length=255)
    distance=models.DecimalField(max_digits=10,decimal_places=2)
    created=models.DateTimeField(auto_now_add=True)

    def __Str__(self):
        return f"Distance from {self.location} to {self.destination} is {self.distance} km"