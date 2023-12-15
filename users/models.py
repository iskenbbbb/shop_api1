from django.contrib.auth.models import User
from django.db import models


class UserConfirm(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    code = models.IntegerField()
