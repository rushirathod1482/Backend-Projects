from django.contrib import admin
from .models import *

@admin.register(Images)
class ImageAdmin(admin.ModelAdmin):
    list_display = ['id','photo','date']
