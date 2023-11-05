from django.contrib import admin
from .models import airConditionerUnits, electricityUnits, gas, dailyHistory

# Register your models here.
admin.site.register(airConditionerUnits)
admin.site.register(electricityUnits)
admin.site.register(gas)
admin.site.register(dailyHistory)
