from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import MenuItem, category, OrderModel

admin.site.register(MenuItem)
admin.site.register(category)
admin.site.register(OrderModel)
