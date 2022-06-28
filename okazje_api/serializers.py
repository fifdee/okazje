from django.core.exceptions import ValidationError
from rest_framework import serializers
from okazje_app.models import Item
import re

from okazje_app.models import Item


class ItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Item
        fields = ['title', 'url', 'image', 'image_url', 'price', 'rating', 'rating_count', 'description']

    def create(self, validated_data):
        item, created = Item.objects.update_or_create(url=validated_data.get('url', None),
                                                      defaults={
                                                          'title': validated_data.get('title', None),
                                                          'image': validated_data.get('image', None),
                                                          'image_url': validated_data.get('image_url', None),
                                                          'price': validated_data.get('price', None),
                                                          'rating': validated_data.get('rating', None),
                                                          'rating_count': validated_data.get('rating_count', None),
                                                          'description': validated_data.get('description', None),
                                                      })
        return item

    # def validate_url(self, data):
    #     items = Item.objects.all()
    #     for item in items:
    #         if item.url == data:
    #             raise ValidationError(message='Przedmiot o takim URL już jest w bazie danych.')
    #
    #     return data
