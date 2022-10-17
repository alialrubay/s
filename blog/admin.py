from atexit import register
from django.contrib import admin
from .models import *
# Register your models here.
admin.site.register(Pictures)
admin.site.register(MyPhoto)
admin.site.register(BookPhoto)
admin.site.register(NameOfWeb)