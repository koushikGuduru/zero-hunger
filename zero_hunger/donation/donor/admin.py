from django.contrib import admin

# Register your models here.
# donor/admin.py

from django.contrib import admin
from .models import Donor, Donation

admin.site.register(Donor)
admin.site.register(Donation)