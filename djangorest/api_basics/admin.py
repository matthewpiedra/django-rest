from django.contrib import admin
from .models import Airplane, Status

# Register your models here.


admin.site.register([Airplane, Status])