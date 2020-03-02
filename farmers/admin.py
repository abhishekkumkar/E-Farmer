from django.contrib import admin
from .models import farmer,labourer,seller
# Register your models here.

admin.site.register([farmer,labourer,seller])

