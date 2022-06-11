from django.core.files.base import ContentFile
from django.db import models
from okazje_app.utils import unique_slugify


class Item(models.Model):
    title = models.CharField(max_length=100)
    image = models.ImageField(null=True, blank=True)
    image_url = models.URLField(null=True, blank=True)
    price = models.CharField(max_length=100)
    url = models.URLField()
    description = models.TextField(null=True, blank=True)
    rating = models.CharField(max_length=100)
    rating_count = models.IntegerField(null=True, blank=True)
    slug = models.SlugField(null=False, unique=True)

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if not self.slug:
            slug_str = self.title[:50]
            unique_slugify(self, slug_str)
            print('unique slug: ' + str(self.slug))

        if not self.image:
            if self.image_url:
                import requests
                res = requests.get(self.image_url, stream=True)
                if res.status_code == 200:
                    self.image = ContentFile(res.raw, name='image')

        return super().save(*args, **kwargs)