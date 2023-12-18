from django.db import models
from authentication.models import User


class UserFollows(models.Model):
    user = models.ForeignKey(
        User,
        related_name="following",
        on_delete=models.CASCADE
    )

    followed_user = models.ForeignKey(
        User,
        related_name="followed_by",
        on_delete=models.CASCADE
    )

    created = models.DateTimeField(auto_now_add=True, db_index=True)

    class Meta:
        unique_together = ('user', 'followed_user')

        ordering = ["-created"]

    def __str__(self):
        return f"{self.followed_user}"
