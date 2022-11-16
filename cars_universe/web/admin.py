from django.contrib import admin

from cars_universe.accounts.models import Profile
from cars_universe.web.models.additive_models import Event
from cars_universe.web.models.models import Car, CarPhoto


@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    pass
