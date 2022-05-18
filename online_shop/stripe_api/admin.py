from django.contrib import admin

from .models import Item, Order


@admin.register(Item)
class ItemAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'price', 'currency')
    search_fields = ('name', )
    list_filter = ('price', 'currency')

admin.site.register(Order)
