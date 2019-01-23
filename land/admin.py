from django.contrib import admin

from leaflet.admin import LeafletGeoAdmin

# Register your models here.


from .models import Parcel, Category, County


admin.site.register(County, LeafletGeoAdmin)


class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']
    list_filter = ['name']
    prepopulated_fields = {'slug': ('name',)}


admin.site.register(Category, CategoryAdmin)


class ParcelAdmin(LeafletGeoAdmin):
    list_display = ['name', 'slug', 'title_number', 'county', 'district', 'added', 'updated', 'geometry', 'description',
                    'category', 'price', 'available']
    list_filter = ['county', 'district', 'added', 'category', 'price', 'available']
    list_editable = ['available', 'price']
    prepopulated_fields = {'slug': ('name',)}


admin.site.register(Parcel, ParcelAdmin)




