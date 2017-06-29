from django.db import models


class Prioridades(models.Model):
    name = models.CharField(max_length=10, null=False)
    fecha_creacion = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

class Remainder(models.Model):

    PRIORIDADES = (
        ("AT", "Alta"),
        ("NR", "Normal"),
        ("BJ", "Baja"),
    )

    id = models.AutoField(primary_key=True)
    titulo = models.CharField(max_length=60)
    descripcion = models.TextField()
    prioridad = models.ForeignKey(Prioridades, related_name='remainder_prioridad')
    prioridad2 = models.CharField(max_length=7, choices=PRIORIDADES)
    fecha = models.DateTimeField()

    def __str__(self):
        return self.titulo