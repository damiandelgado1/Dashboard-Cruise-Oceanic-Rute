from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Room


# Display all Rooms by a Cruise for rent
class ListRoom(ListView):
    model = Room
    template_name = "room/list_room.html"
    context_object_name = "rooms"


# Show detail by a Room
class DetailRoom(DetailView):
    model = Room
    template_name = "room/detail_room.html"
    context_object_name = "room"


# Create a new Room for Rent in the Cruise
class CreateRoom(CreateView):
    model = Room
    fields = [
        "cruise",
        "number",
        "description",
        "bedrooms",
        "bathroom",
        "dining_room",
        "availability",
        "price"
    ]
    template_name = "room/create_room.html"
    success_url = reverse_lazy("home")


# Modify stated Room by a Cruise
class ModifyRoom(UpdateView):
    model = Room
    fields = [
        "availability",
        "price"
    ]
    template_name = "room/modify_room.html"
    success_url = reverse_lazy("home")


# Delete a Room
class DeleteRoom(DeleteView):
    model = Room
    template_name = "room/delete_room.html"
    success_url = reverse_lazy("home")