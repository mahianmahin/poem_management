from django.contrib import admin

from manager.models import *


@admin.register(Poems)
class PoemsAdmin(admin.ModelAdmin):
    list_display = ('id', 'date', 'added_to_book')
