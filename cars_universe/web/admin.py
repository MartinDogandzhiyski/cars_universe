from django.contrib import admin

from cars_universe.accounts.models import Profile
from cars_universe.web.models.additive_models import Event
from cars_universe.web.models.models import Car, Tool, CarPart


@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    list_display = ('name', 'cars_brand')
    list_filter = ('name',)
    ordering = ('date',)
    readonly_fields = ('description',)
    search_fields = ('cars_brand',)


@admin.register(Tool)
class ToolAdmin(admin.ModelAdmin):
    list_display = ('name', 'brand')
    list_filter = ('name',)
    ordering = ('price',)
    readonly_fields = ('brand',)
    search_fields = ('name',)


@admin.register(CarPart)
class PartAdmin(admin.ModelAdmin):
    list_display = ('name', 'brand')
    list_filter = ('brand_for',)
    ordering = ('price',)
    readonly_fields = ('brand',)
    search_fields = ('name',)