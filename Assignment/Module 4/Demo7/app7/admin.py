from django.contrib import admin
from .models import *

# Register your models here.

class userinfoAdmin(admin.ModelAdmin):
    ordering=['id']
    list_display=["name","email","password","age"]
admin.site.register(userinfo,userinfoAdmin)
