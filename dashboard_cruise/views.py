from django.shortcuts import render
from cruise.models import Cruise
from room.models import Room

def home(request):
    cruise = Cruise.objects.all()
    room = Room.objects.all()
    return render(request, "home/base.html", {"cruise": cruise, "room": room})


# # Filter Rooms in the Dashboard
# def filter_rooms_cruises(request):
#     if request.method == "POST":


