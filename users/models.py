from django.db import models
from django.contrib.auth.models import AbstractUser , BaseUserManager
from django.forms import BooleanField, CharField, SlugField
from django.utils.translation import gettext_lazy as _
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.urls import reverse
from django.utils.text import slugify


class CustomUser(AbstractUser):

    class Type(models.TextChoices):
        PATIENT = 'PATIENT', 'patient'
        HEALTHWORKER ='HEALTHWORKER', 'HEALTHWORKER'

    type_choice = Type.PATIENT

    username = models.CharField(max_length=255,blank=True, null=True, unique=False)
    first_name = models.CharField(max_length= 100, blank=True, null=True)
    email = models.CharField(max_length=150, blank=True, unique=True, null=True)
    last_name = models.CharField(max_length=100, blank=True, null=True)
    type = models.CharField(_('Type'), max_length=50, choices=Type.choices)
    slug = models.SlugField(max_length=264, unique=True, null=True)
    contact_information = models.CharField(max_length=255)
    

    REQUIRED_FIELDS = ['username', 'first_name', 'last_name', 'password', 'type']
    USERNAME_FIELD = 'email'



    @property
    def get_full_name(self):
        return self.first_name + ' ' + self.last_name

    def __str__(self):
        return "{}".format(self.email)

    def save(self, *args, **kwargs):
        if self.id:
            self.type = self.type_choice
        return super().save(*args , **kwargs)

    @property
    def is_patient(self):
        return True if self.type.lower() == 'patient' else False 


class PatientProfile(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    gender = models.CharField
    

    def __str__(self):
        return "{}".format(self.user.email)


@receiver(post_save, sender=CustomUser)
def create_user_profile(sender, instance, created, **kwargs):
    if created and instance.type == "patient":
        PatientProfile.objects.create(user=instance)
    elif created and instance.type == "healthworker":
        HeathWorker.objects.create(user=instance)


class HeathWorker(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    specialization = models.CharField(max_length=100 , null = True , blank = True)

    def __str__(self):
        return "Heath Worker {} Profile".format(self.user.email)


