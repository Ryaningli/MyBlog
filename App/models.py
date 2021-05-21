from django.contrib.auth.models import AbstractUser
from django.db import models


# Create your models here.
class User(AbstractUser):
    first_name = None
    last_name = None
    nick_name = models.CharField(max_length=150, blank=True, null=True)

