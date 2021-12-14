from django.contrib import admin

from hospital.models.patients import Patient
from .models.doctors import Doctor
# Register your models here.

admin.site.register(Doctor)
admin.site.register(Patient)