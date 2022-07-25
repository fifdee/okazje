from django.urls import path
from okazje_app.views import Items, ShowImage, ShowThumbnail, GoTo

urlpatterns = [
    path('', Items.as_view(), name='mainpage'),
    path('<slug:slug>/image/', ShowImage.as_view()),
    path('<slug:slug>/thumbnail/', ShowThumbnail.as_view()),
    path('goto/<str:str>/', GoTo.as_view()),
]