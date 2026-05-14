from django.contrib import admin
from .models import Room

# Panel Admin for manage of Entity's
@admin.register(Room)
class RoomAdmin(admin.ModelAdmin):
    list_display = ["cruise", "number", "description", "bedrooms", "bathroom", "dining_room", "availability", "price"]
    list_filter = ["cruise", "number", "availability", "price"]
    search_fields = ["number", "availability", "price"]