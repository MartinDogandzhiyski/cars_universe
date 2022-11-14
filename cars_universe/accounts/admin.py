from django.contrib import admin

from cars_universe.accounts.models import Profile
from cars_universe.web.models import Car, CarPhoto


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
   # inlines = (PetInlineAdmin,)
    list_display = ('first_name', 'last_name')


@admin.register(Car)
class CarAdmin(admin.ModelAdmin):
    list_display = ('name', 'type')


@admin.register(CarPhoto)
class CarPhotoAdmin(admin.ModelAdmin):
    pass
