from django.db import models

# Create your models here.

class Lugar(models.Model):
	nombre 			= models.CharField(max_length=200) 
	descripcion		= models.CharField(max_length=200) 
	foto 			= models.ImageField(upload_to = 'lugares', null=True, blank=False, default = '/media/lugar.jpg' ) 
	latitud			= models.CharField(max_length=20) 
	longitud		= models.CharField(max_length=20) 

	def __str__ (self):
		return self.nombre

class Galeria (models.Model):
	imagen 			= models.ImageField(upload_to = 'galeria', null=True, blank=False) 
	lugar 			= models.ForeignKey(Lugar, on_delete = models.PROTECT) 

	def __str__ (self):
		return self.lugar.nombre

class Tipo_Sitio (models.Model):
	nombre 			= models.CharField(max_length=200) 

	def __str__ (self):
		return self.nombre

class Sitio (models.Model):
	hora_ini		= models.TimeField(max_length=200) 
	hora_fin		= models.TimeField(max_length=200) 
	tipo 			= models.ForeignKey(Tipo_Sitio, on_delete = models.PROTECT) 
	lugar 			= models.ForeignKey(Lugar, on_delete = models.PROTECT) 

	def __str__ (self):
		return self.nombre

class Tipo_Restaurante (models.Model):
	nombre 			= models.CharField(max_length=200) 

	def __str__ (self):
		return self.nombre

class Restaurante (models.Model):
	hora_ini		= models.TimeField(max_length=200) 
	hora_fin		= models.TimeField(max_length=200) 
	tipo 			= models.ForeignKey(Tipo_Restaurante, on_delete = models.PROTECT) 
	lugar 			= models.ForeignKey(Lugar, on_delete = models.PROTECT) 

	def __str__ (self):
		return self.lugar.nombre

class Hotel (models.Model):
	habitaciones	= models.TimeField(max_length=200) 
	camas			= models.TimeField(max_length=200) 
	lugar 			= models.ForeignKey(Lugar, on_delete = models.PROTECT) 

	def __str__ (self):
		return self.lugar.nombre


class Servicio (models.Model):
	nombre 			= models.CharField(max_length=200) 

	def __str__ (self):
		return self.nombre
