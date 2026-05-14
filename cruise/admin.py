from django.contrib import admin
from .models import Cruise

# Panel Admin for manage of Entity's
@admin.register(Cruise)
class CruiseAdmin(admin.ModelAdmin):
    list_display = ["number", "description", "rooms", "availability", "price"]
    list_filter = ["number", "availability", "price"]
    search_fields = ["number", "availability", "price"]