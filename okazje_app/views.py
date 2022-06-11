from okazje_app.models import Item
from django.views.generic import ListView

PAGINATE_NUMBER = 12


# Create your views here.
class Items(ListView):
    model = Item
    template_name = 'okazje_app/okazje.html'
    context_object_name = 'okazje'
    paginate_by = PAGINATE_NUMBER