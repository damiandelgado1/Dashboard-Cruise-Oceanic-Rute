from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Cruise


# Display all Cruise availability in the Dashboard
class ListCruise(ListView):
    model = Cruise
    template_name = ""
    context_object_name = "cruises"


# Show detail by a Cruise
class DetailCruise(DetailView):
    model = Cruise
    template_name = ""
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
    template_name = ""
    success_url = reverse_lazy("")


# Modify stated by a Cruise
class ModifyCruise(UpdateView):
    model = Cruise
    fields = [
        "availability",
        "price"
    ]
    template_name = ""
    success_url = reverse_lazy("")


# Delete a Cruise
class DeleteCruise(DeleteView):
    model = Cruise
    template_name = ""
    success_url = redirect("")