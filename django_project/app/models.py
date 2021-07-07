from django.contrib.auth import get_user_model
from django.db import models

class Car(models.Model):
    car = models.CharField(max_length=128)
    description = models.TextField()
    owner = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
