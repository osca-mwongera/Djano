from django.contrib import admin

from leaflet.admin import LeafletGeoAdmin

from .models import House, Category, District, County

# Register your models here.


class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']
    prepopulated_fields = {'slug': ('name',)}


admin.site.register(Category, CategoryAdmin)


class HouseAdmin(LeafletGeoAdmin):
    list_display = ['name', 'slug', 'category', 'price', 'stock', 'available', 'time_added', 'updated']
    list_filter = ['available', 'time_added', 'updated', 'category']
    list_editable = ['price', 'stock', 'available']
    prepopulated_fields = {'slug': ('name',)}


admin.site.register(House, HouseAdmin)


admin.site.register(District, LeafletGeoAdmin)


admin.site.register(County, LeafletGeoAdmin)
