from collections.abc import Collection
from django.db import models
from django.contrib.auth import get_user_model

from .mixins import PatientDoctorFieldMixin


User = get_user_model()

# Create your models here.
class MedicalRecord( PatientDoctorFieldMixin , models.Model):
    # MedicalRecord-specific fields
    patient = models.ForeignKey(User, on_delete=models.CASCADE)
    physician = models.ForeignKey(User , on_delete = models.CASCADE)
    admission_date = models.DateField()
    discharge_date = models.DateField()
    diagnosis = models.TextField()
    treatment = models.TextField()
    prescriptions = models.TextField()

    def clean_fields(self, exclude= None) -> None:
        super().clean_fields(exclude)

        self.clean_patient_doctor(self.patient , self.physician)


class Appointment(PatientDoctorFieldMixin , models.Model):
    # Appointment-specific fields
    patient = models.ForeignKey(User, on_delete=models.CASCADE)
    health_practioner = models.ForeignKey(User, on_delete=models.CASCADE)
    appointment_date = models.DateTimeField()
    notes = models.TextField()

    class Meta:
        ordering = ['appointment_date']

    def clean_fields(self, exclude= None) -> None:
        super().clean_fields(exclude)

        self.clean_patient_doctor(self.patient , self.health_practioner)