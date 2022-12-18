from django.contrib import admin
from .models import Shops


class shopsAdmin(admin.ModelAdmin):
    list_display = ('name', 'location',)
    list_filter = ('name',)
    
    search_fields = ('name','description','location',)
    ordering = ('name',)
    filter_horizontal = ()
    

admin.site.register(Shops, shopsAdmin)
