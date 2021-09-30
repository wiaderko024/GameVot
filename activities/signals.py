from django.db.models.signals import post_save
from .models import Activity
from reviews.models import Review, Rate
from games.models import Game


def create_review_activity(sender, instance, created, **kwargs):
    if created:
        Activity.objects.create(review=True, review_id=instance, user=instance.user)

        game = Game.objects.get(pk=instance.game.id)
        game.reviews += 1
        game.save()


def create_rate_activity(sender, instance, created, **kwargs):
    if created:
        Activity.objects.create(rate=True, rate_id=instance, user=instance.user)

        game = Game.objects.get(pk=instance.game.id)
        game.rates += 1

        if game.avg_rate is None:
            game.avg_rate = float(instance.rate)
        else:
            rates = Rate.objects.filter(game=game)

            tmp = 0
            for rate in rates:
                tmp += rate.rate

            game.avg_rate = tmp / len(rates)

        game.save()


post_save.connect(create_review_activity, Review)
post_save.connect(create_rate_activity, Rate)
