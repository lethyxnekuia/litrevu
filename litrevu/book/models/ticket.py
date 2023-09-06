from django.db import models
from authentication.models import User

class Ticket(models.Model):
    title = models.CharField(max_length=128)
    description = models.TextField(max_length=128, blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    image = models.ImageField(blank=True, null=True)
    time_created = models.DateTimeField(auto_now_add=True)