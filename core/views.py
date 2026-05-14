from django.shortcuts import render
from cruise.models import Cruise
from room.models import Room

# Home page of the Dashboard
def dashboard_home(request):
    cruises = Cruise.objects.all()
    rooms = Room.objects.all()
    return render(request, "home/dashboard.html", {"cruises": cruises, "rooms": rooms})