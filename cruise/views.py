from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Cruise


# Display all Cruise availability in the Dashboard
class ListCruise(ListView):
    model = Cruise
    template_name = "cruise/list_cruise.html"
    context_object_name = "cruises"


# Show detail by a Cruise
class DetailCruise(DetailView):
    model = Cruise
    template_name = "cruise/detail_cruise.html"
    context_object_name = "cruise"


# Create a Cruise for travel
class CreateCruise(CreateView):
    model = Cruise
    fields = [
        "number",
        "description",
        "rooms",
        "availability",
        "price"
    ]
    template_name = "cruise/create_cruise.html"
    success_url = reverse_lazy("home")


# Modify stated by a Cruise
class ModifyCruise(UpdateView):
    model = Cruise
    fields = [
        "availability",
        "price"
    ]
    template_name = "cruise/modify_cruise.html"
    success_url = reverse_lazy("home")


# Delete a Cruise
class DeleteCruise(DeleteView):
    model = Cruise
    template_name = "cruise/delete_cruise.html"
    success_url = reverse_lazy("home")