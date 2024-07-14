from django.db import models

class Turno(models.Model):
    nombre = models.CharField(max_length=100)
    correo = models.EmailField()
    telefono = models.CharField(max_length=15)
    tipo_clase = models.CharField(max_length=100)
    fecha_hora = models.DateTimeField()

    def __str__(self):
        return f"{self.nombre} - {self.tipo_clase}"
