from django.urls import path
from okazje_app.views import Items

urlpatterns = [
    path('', Items.as_view()),
]