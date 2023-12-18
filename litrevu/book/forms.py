from django import forms
from . import models


class TicketForm(forms.ModelForm):
    class Meta:
        model = models.Ticket
        fields = ['title', 'description', 'image']


class ReviewForm(forms.ModelForm):
    RATING_CHOICES = (
        (1, "One"),
        (2, "Two"),
        (3, "Three"),
        (4, "Four"),
        (5, "Five"),
    )

    rating = forms.ChoiceField(choices=RATING_CHOICES, label="Note")

    class Meta:
        model = models.Review
        fields = ['headline', 'rating', 'body']
