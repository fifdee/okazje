from django.core.files.base import ContentFile
from django.db import models
from okazje_app.utils import unique_slugify, create_image


class Item(models.Model):
    title = models.CharField(max_length=256)
    image = models.ImageField(null=True, blank=True)
    image_thumbnail = models.ImageField(null=True, blank=True)
    image_url = models.URLField(null=True, blank=True)
    price = models.CharField(max_length=100)
    url = models.URLField()
    description = models.TextField(null=True, blank=True)
    rating = models.CharField(max_length=256, null=True, blank=True)
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
                    self.image = ContentFile(create_image(res.content, 1280), name='image')
                    self.image_thumbnail = ContentFile(create_image(self.image, 384), name='thumbnail')

        if self.image:
            if not self.image_thumbnail:
                self.image_thumbnail = ContentFile(create_image(self.image, 384), name='thumbnail')

        return super().save(*args, **kwargs)