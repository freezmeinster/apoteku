from django.contrib import admin
from .models import Pelanggan, Resep, BarisResep

class BarisResepAdmin(admin.TabularInline):
   model = BarisResep

class ResepAdmin(admin.ModelAdmin):
   inlines = [ BarisResepAdmin, ]

admin.site.register(Pelanggan)
admin.site.register(Resep, ResepAdmin)
