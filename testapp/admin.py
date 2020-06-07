from django.contrib import admin

from .models import *
admin.site.register(Book)
admin.site.register(BookOrdered)
admin.site.register(BookTheme)
admin.site.register(Order)
admin.site.register(Reader)