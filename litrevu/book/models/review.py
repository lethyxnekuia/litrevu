from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from .ticket import Ticket
from authentication.models import User

class Review(models.Model):
    ticket = models.ForeignKey(Ticket, related_name="reviews", on_delete=models.CASCADE)
    rating = models.PositiveIntegerField(validators=[MinValueValidator(0), MaxValueValidator(5)])
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    headline = models.CharField(max_length=128)
    body = models.TextField(max_length=8192, blank=True)
    time_created = models.DateTimeField(auto_now_add=True)