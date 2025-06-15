from django.contrib import admin
from concession.models import Concession

class ConcessionAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'roll', 'year', 'branch', 'start_dest', 'end_dest', 'period')

admin.site.register(Concession,ConcessionAdmin)