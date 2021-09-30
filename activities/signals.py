from django.db.models.signals import post_save
from .models import Activity
from reviews.models import Review, Rate


def create_review_activity(sender, instance, created, **kwargs):
    if created:
        Activity.objects.create(review=True, review_id=instance, user=instance.user)


def create_rate_activity(sender, instance, created, **kwargs):
    if created:
        Activity.objects.create(rate=True, rate_id=instance, user=instance.user)


post_save.connect(create_review_activity, Review)
post_save.connect(create_rate_activity, Rate)
