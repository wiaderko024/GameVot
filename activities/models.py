from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from games.models import Game
from reviews.models import Review, Rate


class Activity(models.Model):
    visit = models.BooleanField(default=False, blank=False, null=False)
    review = models.BooleanField(default=False, blank=False, null=False)
    rate = models.BooleanField(default=False,blank=False, null=False)
    game = models.ForeignKey(Game, on_delete=models.DO_NOTHING, blank=True, null=True)
    review_id = models.ForeignKey(Review, on_delete=models.DO_NOTHING, blank=True, null=True)
    rate_id = models.ForeignKey(Rate, on_delete=models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(User, on_delete=models.DO_NOTHING, blank=False, null=False)
    created_at = models.DateTimeField(default=timezone.now, editable=False)

    def ___str__(self):
        if self.visit:
            return 'visit - ' + self.game.title
        elif self.review:
            return 'review - ' + self.review.game.title
        elif self.rate:
            return 'rate - ' + self.rate.game.title
        else:
            return 'NOTHING'

    def save(self, *args, **kwargs):
        if not self.created_at:
            self.created_at = timezone.now()

        return super(Activity, self).save(*args, **kwargs)
