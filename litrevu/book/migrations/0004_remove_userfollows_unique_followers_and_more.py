# Generated by Django 4.2.4 on 2023-10-11 17:22

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('book', '0003_userfollows_userfollows_unique_followers'),
    ]

    operations = [
        migrations.RemoveConstraint(
            model_name='userfollows',
            name='unique_followers',
        ),
        migrations.AlterUniqueTogether(
            name='userfollows',
            unique_together={('user', 'followed_user')},
        ),
    ]
