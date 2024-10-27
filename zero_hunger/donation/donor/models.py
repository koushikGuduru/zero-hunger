from django.db import models

# Create your models here.


# donor/models.py

from django.contrib.auth.models import User
from django.db import models
from django.contrib.auth.hashers import make_password

class Donor(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone_number = models.CharField(max_length=15)
    password = models.CharField(max_length=128)  # Store hashed password

    def __str__(self):
        return self.user.username

    def save(self, *args, **kwargs):
        # Hash the password before saving
        if self.password:
            self.password = make_password(self.password)
        super().save(*args, **kwargs)

class Donation(models.Model):
    donor = models.ForeignKey(User, on_delete=models.CASCADE)
    item = models.CharField(max_length=100)
    donation_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.item} donated by {self.donor.username}"