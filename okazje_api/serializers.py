from django.core.exceptions import ValidationError
from rest_framework import serializers
from django.core.files.base import ContentFile

from okazje_app.models import Item


class ItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Item
        fields = ['title', 'url', 'image', 'price', 'rating', 'rating_count']

    def validate_url(self, data):
        items = Item.objects.all()
        for item in items:
            if item.url == data:
                raise ValidationError(message='Przedmiot o takim URL już jest w bazie danych.')

        return data

    def validate_image(self, data):
        import requests
        res = requests.get(data, stream=True)
        if res.status_code == 200:
            image = ContentFile(res.raw, name='image')
            return image
        else:
            raise ValidationError(message='Problem z pobraniem obrazka.')
