from django.db import models

# Create your models here.


# receiver/models.py

from django.db import models
from django.contrib.auth.models import User

class Receiver(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone_number = models.CharField(max_length=15)

    def __str__(self):
        return self.user.username