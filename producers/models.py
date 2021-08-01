from django.db import models
from django_countries.fields import CountryField
from django.utils.text import slugify


class Producer(models.Model):
    name = models.CharField(max_length=128, blank=False, null=False)
    description = models.TextField(default='', blank=False, null=False)
    year = models.IntegerField(default=2000, blank=False, null=False)
    country = CountryField(blank=True, null=True)
    logo = models.ImageField(upload_to='producers_logo', blank=True, null=True)
    slug = models.SlugField(null=True, editable=False)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)

        return super(Producer, self).save(*args, **kwargs)
