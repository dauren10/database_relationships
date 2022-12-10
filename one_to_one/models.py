from django.db import models

class CurrentAddress(models.Model):
    city = models.CharField(max_length=50)
    address = models.CharField(max_length=80)

    def __str__(self):
        return "%s the place" % self.city

class Person(models.Model):
    address = models.OneToOneField(
        CurrentAddress,
        on_delete=models.CASCADE,
        primary_key=True,
    )
    name = models.CharField(max_length=80)

    def __str__(self):
        return "%s the restaurant" % self.address.address

