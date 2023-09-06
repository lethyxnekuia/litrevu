from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):

    profile_photo = models.ImageField()
    follows = models.ManyToManyField(
        'self',
        symmetrical=False,
        related_name='followed_by'
    )

    def __str__(self):
        return f'{self.username}'
