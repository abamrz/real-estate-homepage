from django.contrib import admin
from .models import Realtor


# Register your models here.
class RealtorAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'is_mvp', 'email')
    list_filter = ('is_mvp',)
    search_fields = ('name', 'is_mvp')


admin.site.register(Realtor, RealtorAdmin)
