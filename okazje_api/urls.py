from django.urls import path, include
from rest_framework import routers
from .views import ItemApiViewSet

router = routers.DefaultRouter()
router.register('okazje', ItemApiViewSet)


urlpatterns = [
    path('', include(router.urls)),
]