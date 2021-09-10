from django.db import models
from django.contrib.auth.models import User
from games.models import Game
from django.utils import timezone


class Review(models.Model):
    user = models.ForeignKey(User, on_delete=models.DO_NOTHING, blank=False, null=False)
    game = models.ForeignKey(Game, on_delete=models.DO_NOTHING, blank=False, null=False)
    text = models.TextField(default='', blank=False, null=False)
    created_at = models.DateTimeField(editable=False, null=False)

    def __str__(self):
        return self.user.username

    def save(self, *args, **kwargs):
        if not self.created_at:
            self.created_at = timezone.now()

        return super(Review, self).save(*args, **kwargs)


class Rate(models.Model):
    scale = [(i, i) for i in range(1, 11)]

    user = models.ForeignKey(User, on_delete=models.DO_NOTHING, blank=False, null=False)
    game = models.ForeignKey(Game, on_delete=models.DO_NOTHING, blank=False, null=False)
    rate = models.PositiveSmallIntegerField(editable=True, choices=scale, blank=False, null=False)

    def __str__(self):
        return user.username + ' - ' + str(rate)
