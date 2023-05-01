from django.db import models


# Create your models here.

class Canteen(models.Model):
    """Model representing a canteen."""
    name = models.CharField(
        max_length=200,
        help_text="Enter a Canteen"
    )
    location = models.CharField(max_length=200)
    

    def __str__(self):
        """String for representing the Model object (in Admin site etc.)"""
        return self.name
