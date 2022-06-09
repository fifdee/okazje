from rest_framework.viewsets import ModelViewSet
from rest_framework_api_key.permissions import HasAPIKey
from rest_framework import authentication

from okazje_app.models import Item
from .serializers import ItemSerializer


class ItemApiViewSet(ModelViewSet):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer
    authentication_classes = [authentication.RemoteUserAuthentication]
    permission_classes = [HasAPIKey]

    def perform_create(self, serializer):
        serializer.save()

