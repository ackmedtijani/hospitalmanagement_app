from django.core.exceptions import ValidationError

class PatientDoctorFieldMixin:

    def clean_patient_doctor(self , patient , doctor):
        if patient.type != "patient" and doctor.type != "doctor":
            raise ValidationError("A patient can't assign medical record to a doctor or another patient")