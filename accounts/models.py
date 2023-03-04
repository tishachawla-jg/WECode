from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    is_HR = models.BooleanField()

    def __str__(self):
        return str(f'{self.user.id}' + ' ' + f'{self.user.username}' + ' ' + f'{self.is_HR}')
