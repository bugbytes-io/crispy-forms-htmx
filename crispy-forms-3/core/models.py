from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class User(AbstractUser):

    class Subjects(models.IntegerChoices):
        WEB_DEVELOPMENT = 1
        SYSTEMS_PROGRAMMING = 2
        DATA_SCIENCE = 3
    
    subject = models.PositiveSmallIntegerField(choices=Subjects.choices)
    date_of_birth = models.DateField()