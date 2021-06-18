from django.contrib import admin
from .models import Airplanes, AirplaneStatus

# Register your models here.


admin.site.register([Airplanes, AirplaneStatus])