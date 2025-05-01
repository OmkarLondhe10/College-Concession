from django.contrib import admin
from service.models import services

class servicesAdmin(admin.ModelAdmin):
    list_display=('name','email','subject','message')
# Register your models here.

admin.site.register(services,servicesAdmin)