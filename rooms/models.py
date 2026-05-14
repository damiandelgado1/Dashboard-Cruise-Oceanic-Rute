from django.db import models
from cruise.models import Cruise

# Details of the Room by a Cruise
class Room(models.Model):
    cruise = models.ForeignKey(Cruise, on_delete=models.CASCADE, verbose_name="Crucero de la Habitacion")
    number = models.IntegerField(verbose_name="Nro. de la Habitacion")
    preview = models.CharField(max_length=10000, verbose_name="Preview de la Habitacion")
    description = models.TextField(verbose_name="Descripcion de la Habitacion")
    bedrooms = models.IntegerField(verbose_name="Nro. de Dormitorios")
    bathroom = models.CharField(max_length=10, verbose_name="Nro. de Baños")
    dining_room = models.CharField(max_length=10, verbose_name="Comedor")
    availability = models.CharField(max_length=20, verbose_name="Estado de la Habitacion")
    price = models.DecimalField(max_digits=6, decimal_places=3, null=False, verbose_name="Precio de la Habitacion")

    def __str__(self):
        return f"Habitacion {self.number}: {self.availability}"

    class Meta:
        verbose_name = "room"
        verbose_name_plural = "rooms"