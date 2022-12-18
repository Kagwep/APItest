from django.contrib import admin
from .models import Products


class productAdmin(admin.ModelAdmin):
    list_display = ('name', 'sold',)
    list_filter = ('sold',)
    
    search_fields = ('name',)
    ordering = ('name',)
    filter_horizontal = ()
    

admin.site.register(Products, productAdmin)