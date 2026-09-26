from django.shortcuts import render
from cruise.models import Cruise
from room.models import Room

def home(request):
    cruises = Cruise.objects.all()
    rooms = Room.objects.all()
    return render(request, "home/base.html", {"cruises": cruises, "rooms": rooms})