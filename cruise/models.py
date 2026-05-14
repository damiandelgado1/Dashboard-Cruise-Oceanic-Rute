from django.db import models

# Data and Information about Cruise
class Cruise(models.Model):
    number = models.IntegerField(null=True, verbose_name="Nro. del Crucero")
    description = models.TextField(verbose_name="Descripcion del Crucero")
    rooms = models.IntegerField(null=False, verbose_name="Nro. de Habitaciones")
    availability = models.CharField(max_length=20, null=False, verbose_name="Estado del Crucero")
    price = models.DecimalField(max_digits=6, decimal_places=3, null=False, verbose_name="Precio del Crucero")

    def __str__(self):
        return f"Crucero: {self.number}"

    class Meta:
        verbose_name = "cruise"
        verbose_name_plural = "cruises"