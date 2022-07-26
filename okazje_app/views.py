from django.views import View

from okazje_app.models import Item
from django.views.generic import ListView
from django.shortcuts import HttpResponse, get_object_or_404, redirect

PAGINATE_NUMBER = 12


# Create your views here.
class Items(ListView):
    model = Item
    template_name = 'okazje_app/okazje.html'
    context_object_name = 'okazje'
    paginate_by = PAGINATE_NUMBER


class ItemsDirect(ListView):
    model = Item
    template_name = 'okazje_app/okazje.html'
    context_object_name = 'okazje'
    paginate_by = PAGINATE_NUMBER

    def get_context_data(self, **kwargs):
        context = super(ItemsDirect, self).get_context_data(**kwargs)
        context['details_active'] = True

        return context


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


class GoTo(View):
    def get(self, request, slug, *args, **kwargs):
        obj = get_object_or_404(klass=Item, slug=slug)
        obj.clicks += 1
        obj.save()

        return redirect(obj.url)
