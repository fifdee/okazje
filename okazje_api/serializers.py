from django.core.exceptions import ValidationError
from rest_framework import serializers
import re

from okazje_app.models import Item


class ItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Item
        fields = ['title', 'url', 'image', 'image_url', 'price', 'rating', 'rating_count', 'description']

    def validate_url(self, data):
        items = Item.objects.all()
        for item in items:
            if item.url == data:
                raise ValidationError(message='Przedmiot o takim URL już jest w bazie danych.')

        return data
