from django.contrib import admin

from .models import CurrentAddress,Person

admin.site.register(CurrentAddress)
admin.site.register(Person)