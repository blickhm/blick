from django.db import models

# Create your models here.
class Precio(models.Model):
    precio = models.DecimalField(max_digits = 8,decimal_places = 2)

    def __str__(self):
        return str(self.precio)

class Producto(models.Model):
    nombre = models.CharField(max_length = 40)
    descripcion = models.TextField()
    imagen = models.FileField(upload_to='commerce/media',default='algo.jpg')

    def __str__(self):
        return self.nombre

class Usuario(models.Model):
    nombre = models.CharField(max_length = 30)
    apellidos = models.CharField(max_length = 30)
    email = models.EmailField(max_length = 90)
    password = models.CharField(max_length = 50)

    def __str__(self):
        return self.nombre + ' ' + self.apellidos

class Clasificacion(models.Model):
    nombre = models.CharField(max_length = 20)

    def __str__(self):
        return self.nombre

class Empresa(models.Model):
    nombre = models.CharField(max_length = 50)
    latitud = models.DecimalField(max_digits = 20, decimal_places = 18)
    longitud = models.DecimalField(max_digits = 20, decimal_places = 18)
    telefono = models.IntegerField()
    direccion = models.TextField()
    descripcion =  models.TextField(default='desconocida')
    clasificacion = models.ForeignKey(Clasificacion)
    usuario = models.ForeignKey(Usuario)

    def __str__(self):
        return self.nombre

class Producto_precio(models.Model):
    precio = models.ForeignKey(Precio)
    product = models.ForeignKey(Producto)
    empresa = models.ForeignKey(Empresa)
    def __str__(self):
        return str(self.product) + ': $' + str(self.precio)

class Pedido(models.Model):
    comentario = models.TextField()
    latitud = models.DecimalField(max_digits = 20, decimal_places = 18)
    longitud = models.DecimalField(max_digits = 20, decimal_places = 18)
    empresa = models.ForeignKey(Empresa)
    productos = models.ManyToManyField(Producto_precio)

    def __str__(self):
        return self.primary_key