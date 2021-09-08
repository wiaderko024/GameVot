from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    avatar = models.ImageField(upload_to='avatars', blank=True, null=True)
    created_at = models.DateTimeField(default=timezone.now, editable=False, null=False)

    def __str__(self):
        return self.user.username

    def save(self, *args, **kwargs):
        if not self.created_at:
            self.created_at = timezone.now()

        return super(Profile, self).save(*args, **kwargs)
