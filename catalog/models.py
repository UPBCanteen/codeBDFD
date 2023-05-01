from django.db import models


# Create your models here.


class Canteen(models.Model):
    """Model representing a canteen."""
    name = models.CharField(
        max_length=200,
        help_text="Enter a Canteen"
    )
    location = models.CharField(max_length=200)
    schedule = models.CharField(max_length=200)

    def __str__(self):
        """String for representing the Model object (in Admin site etc.)"""
        return self.name


class Meal(models.Model):
    name = models.CharField(max_length=200)
    quantity = models.IntegerField()
    remainQuantity = models.IntegerField()
    canteen = models.ForeignKey(Canteen, on_delete=models.CASCADE)


class UserType(models.Model):
    userType = models.CharField(
        max_length=20,
        help_text="Enter a user type"
    )

    def _str_(self):
        """String for representing the Model object (in Admin site etc.)"""
        return self.userType


class Person(models.Model):
    username = models.CharField(
        max_length=20,
        unique=True,
        help_text="Enter a username"
    )

    email = models.CharField(
        max_length=100,
        unique=True,
        help_text="Enter a email"
    )

    password = models.CharField(max_length=100)

    userType = models.ManyToManyField(UserType)

    def _str_(self):
        """String for representing the Model object (in Admin site etc.)"""
        return self.username


class MealQuantity(models.Model):
    meal = models.ForeignKey(Meal, on_delete=models.CASCADE)
    quantity = models.IntegerField()


class Order(models.Model):
    canteen = models.ForeignKey(Canteen, on_delete=models.CASCADE)
    mealQuantity = models.ManyToManyField(MealQuantity)
    time = models.DateTimeField()
