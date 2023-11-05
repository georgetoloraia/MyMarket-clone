from mptt.admin import DraggableMPTTAdmin
from .models import Category 
from items.models import Item
from django.contrib import admin

class CategoryAdmin(DraggableMPTTAdmin):
    mptt_indent_field = "name"
    list_display = ('tree_actions', 'indented_title',
                    'related_products_count', 'related_products_cumulative_count')
    list_display_links = ('indented_title',)

    def get_queryset(self, request):
        qs = super().get_queryset(request)

        # Add cumulative product count
        qs = Category.objects.add_related_count(
                qs,
                Item,
                'category',
                'products_cumulative_count',
                cumulative=True)
 
        # Add non cumulative product count
        qs = Category.objects.add_related_count(qs,
                 Item,
                 'category',
                 'products_count',
                 cumulative=False)
        return qs

    def related_products_count(self, instance):
        return getattr(instance, 'products_count', None)
    related_products_count.short_description = 'Related products (for this specific category)'

    def related_products_cumulative_count(self, instance):
        return getattr(instance, 'products_cumulative_count', None)
    related_products_cumulative_count.short_description = 'Related products (in tree)'


admin.site.register(Category , CategoryAdmin)