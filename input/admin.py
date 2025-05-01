from django.contrib import admin

# Register your models here.
from input.models import output

class outputAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'year', 'branch', 'start_destination', 'end_destination')

admin.site.register(output,outputAdmin)