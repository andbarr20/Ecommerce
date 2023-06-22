from django.db import models
from django.urls import reverse

# Create your models here.
class Genero(models.Model):
    name = models.CharField(max_length=200, help_text="Ingrese el nombre del genero")

    def __str__(self):
        return self.name

class Lenguaje(models.Model):
    nombre = models.CharField(max_length=200, help_text="Ingrese el lenguaje del libro")

    def __str__(self):
        return self.nombre

class Libro(models.Model):
    titulo = models.CharField(max_length=200)
    autor = models.ForeignKey('Autor', on_delete=models.SET_NULL, null=True)
    resumen = models.TextField(max_length=1000, help_text="Ingrese una breve descripción del libro")
    isbn = models.CharField('ISBN', max_length=13, help_text='13 Caracteres <a href="https://www.isbn-international.org/content/what-isbn">ISBN number</a>')
    genero = models.ManyToManyField(Genero, help_text="Seleccione un genero para este libro")
    lenguaje = models.ForeignKey('Lenguaje', on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.titulo
    
    def get_absolute_url(self):
        return reverse('book-detail', args=[str(self.id)])

import uuid 

class BookInstance(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, help_text="ID unico para este libro particular en toda la biblioteca")
    libro = models.ForeignKey('libro', on_delete=models.SET_NULL, null=True)
    imprint = models.CharField(max_length=200)
    due_back = models.DateField(null=True, blank=True)

    LOAN_STATUS = (
        ('m', 'maintance'),
        ('o', 'On loan'),
        ('a', 'Available'),
        ('r', 'Reserved'),
    )

    status = models.CharField(max_length=1, choices= LOAN_STATUS, blank=True, default='m', help_text='Disponibilidad del libro')

class Meta:
    ordering = ["due_back"]

def __str__(self):
    return '%s (%s)' % (self.id,self.libro.titulo)

class Autor(models.Model):
    primer_nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    fecha_de_nacimiento = models.DateField(null=True, blank=True)
    fecha_de_fallecimiento = models.DateField('Died', null=True, blank=True)

    def get_absolute_url(self):
        return reverse('detalles_autor', args=[str(self.id)])

    def __str__(self):
        return '%s, %s' % (self.apellido, self.primer_nombre)