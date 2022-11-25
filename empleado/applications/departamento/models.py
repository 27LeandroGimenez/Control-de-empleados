from django.db import models

# Create your models here.

class Departamento(models.Model):
    name = models.CharField('Nombre', max_length=50)
    shor_name = models.CharField('Nombre corto', max_length=20)
    anulado = models.BooleanField('Anulado', default=False)

    class Meta:
        verbose_name = 'Departamento'
        verbose_name_plural = 'Departamentos'
        ordering = ['-id']
        unique_together = ('name', 'shor_name')


    def __str__(self):
        return str(self.id) + ' - ' + self.name + ' - ' + self.shor_name
