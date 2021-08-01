from django.db import models
from django.utils.text import slugify


class Category(models.Model):
    name = models.CharField(max_length=128, blank=False, null=False)
    icon = models.CharField(max_length=128, blank=False, null=False)
    description = models.TextField(default='', blank=False, null=False)
    slug = models.SlugField(null=True, editable=False)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)

        return super(Category, self).save(*args, **kwargs)
