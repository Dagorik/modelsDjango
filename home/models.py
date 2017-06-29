from django.db import models


class Prioridad(models.Model):
    name = models.CharField(max_length=10, null=False)
    fecha_creacion = models.DateTimeField(auto_now=True)

    def __str__(self):
        return "El nombre es " + self.name

class Remainder(models.Model):

    PRIORIDADES = (
        ("AT", "Alta"),
        ("NR", "Normal"),
        ("BJ", "Baja"),
    )

    MEDIA_CHOICES = (
    ('Audio', (
            ('vinyl', 'Vinyl'),
            ('cd', 'CD'),
        )
    ),
    ('Video', (
            ('vhs', 'VHS Tape'),
            ('dvd', 'DVD'),
        )
    ),
    ('unknown', 'Unknown'),
)

    id = models.AutoField(primary_key=True)
    titulo = models.CharField(max_length=60)
    descripcion = models.TextField()
    prioridad = models.ForeignKey(Prioridad, related_name='remainder_prioridad')
    prioridad2 = models.CharField(max_length=7, choices=MEDIA_CHOICES)
    fecha = models.DateTimeField()

    def __str__(self):
        return self.titulo