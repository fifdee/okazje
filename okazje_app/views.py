from django.views import View

from okazje_app.models import Item
from django.views.generic import ListView
from django.shortcuts import HttpResponse, get_object_or_404

PAGINATE_NUMBER = 12


# Create your views here.
class Items(ListView):
    model = Item
    template_name = 'okazje_app/okazje.html'
    context_object_name = 'okazje'
    paginate_by = PAGINATE_NUMBER


class ShowImage(View):
    def get(self, request, slug, *args, **kwargs):
        item = get_object_or_404(Item, slug=slug)

        image = item.image

        return HttpResponse(image, content_type='image/png')


class ShowThumbnail(View):
    def get(self, request, slug, *args, **kwargs):
        item = get_object_or_404(Item, slug=slug)

        image = item.image_thumbnail

        return HttpResponse(image, content_type='image/webp')