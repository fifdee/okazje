from django.core.validators import validate_comma_separated_integer_list
from django.db import models
from okazje_app.utils import unique_slugify


class Item(models.Model):
    title = models.CharField(max_length=100)
    image = models.ImageField()
    price = models.CharField(max_length=100)
    url = models.URLField()
    description = models.TextField(null=True, blank=True)
    rating = models.CharField(max_length=100, validators=[validate_comma_separated_integer_list])
    rating_count = models.IntegerField(null=True, blank=True)
    slug = models.SlugField(null=False, unique=True)

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if not self.slug:
            slug_str = self.title[:50]
            unique_slugify(self, slug_str)
            print('unique slug: ' + str(self.slug))

        return super().save(*args, **kwargs)