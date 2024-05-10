# models.py

from djongo import models

class Employee(models.Model):
    first_name = models.CharField(max_length=100)
    second_name = models.CharField(max_length=100, blank=True)
    third_name = models.CharField(max_length=100, blank=True)
    email = models.EmailField()

    def __str__(self):
        return self.first_name
