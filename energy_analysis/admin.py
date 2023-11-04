from django.contrib import admin
from .models import airConditionerUnits, electricityUnits, gas

# Register your models here.
admin.site.register(airConditionerUnits)
admin.site.register(electricityUnits)
admin.site.register(gas)
