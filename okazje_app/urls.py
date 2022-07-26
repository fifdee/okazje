from django.urls import path
from okazje_app.views import Items, ShowImage, ShowThumbnail, GoTo, ItemsDirect

urlpatterns = [
    path('', Items.as_view(), name='mainpage'),
    path('details_active/', ItemsDirect.as_view(), name='mainpage_details_active'),
    path('<slug:slug>/image/', ShowImage.as_view()),
    path('<slug:slug>/thumbnail/', ShowThumbnail.as_view()),
    path('goto/<slug:slug>/', GoTo.as_view(), name='goTo'),
]