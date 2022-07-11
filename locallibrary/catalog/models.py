from django.db import models
from django.urls import reverse

# Create your models here.
class Listado(models.Model):
    #fields
    id= models.AutoField(primary_key=True)
    name = models.CharField(max_length=20, help_text='Nombre del producto', verbose_name='Nombre del producto')
    description = models.CharField(max_length=100, help_text='Descripción', verbose_name='Descripción')
    price = models.PositiveIntegerField(null=True, verbose_name='Precio')
    image = models.ImageField(upload_to='imagenes/', null=True, verbose_name='Imagen')

    #metadata
    class Meta:
        ordering = ['-price']

    #methods
    def get_absolute_url(self):
        #returns the url to access a particular instance of Listado
        return reverse('model-detail-view', args=[str(self.id)])

    def __str__(self):
        #string for representing Listado object
        return self.name

    def delete(self, using=None, keep_parents=False):
        #Se sobrescribe el metodo delete para poder borrar fisicamente las imagenes
        #self.image.storage.delete(self.image.name)
        super().delete()
