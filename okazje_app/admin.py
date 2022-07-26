from django.contrib import admin

# Register your models here.
from okazje_app.models import Item


class ItemAdmin(admin.ModelAdmin):
    search_fields = ['title']


admin.site.register(Item, ItemAdmin)