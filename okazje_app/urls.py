from django.urls import path
from okazje_app.views import Items, ShowImage, ShowThumbnail

urlpatterns = [
    path('', Items.as_view()),
    path('<slug:slug>/image/', ShowImage.as_view()),
    path('<slug:slug>/thumbnail/', ShowThumbnail.as_view()),
]