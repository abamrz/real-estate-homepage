from django.contrib import admin
from .models import Listing


# Register your models here.
class ListingAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'price', 'realtor', 'is_published')
    list_display_links = ('id', 'title')
    list_filter = ('realtor', 'price')
    list_editable = ('is_published',)
    search_fields = ('title', 'description', 'address', 'city', 'state', 'zipcode', 'price')
    list_per_page = 20


admin.site.register(Listing, ListingAdmin)

