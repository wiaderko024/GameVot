from django.db import models
from django.utils.text import slugify
from producers.models import Producer


class Game(models.Model):
    title = models.CharField(max_length=300, blank=False, null=False, unique=True)
    year = models.IntegerField(default=2000, blank=False, null=False)
    description = models.TextField(default="", blank=True, null=True)
    cover = models.ImageField(upload_to='game_covers', blank=True, null=True)
    producer = models.ForeignKey(Producer, on_delete=models.DO_NOTHING, null=True, blank=True)
    slug = models.SlugField(null=True, editable=False)

    def __str__(self):
        return self.title + ' ' + str(self.year)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)

        return super(Game, self).save(*args, **kwargs)
