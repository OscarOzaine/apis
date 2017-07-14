from django.db import models

class Representatives(models.Model):

	id = models.IntegerField(primary_key=True)
	nombre = models.CharField(max_length=255, blank=True, default='')
	created_at = models.DateTimeField(auto_now_add=True)
	slug = models.CharField(max_length=255, blank=True, default='')
	zona = models.CharField(max_length=255, blank=True, default='')
	estatus = models.CharField(max_length=255, blank=True, default='')
	ultimo_grado_de_estudios = models.CharField(max_length=255, blank=True, default='')
	partido = models.CharField(max_length=255, blank=True, default='')
	telefono_en_camara = models.CharField(max_length=255, blank=True, default='')
	preparacion_academica = models.CharField(max_length=255, blank=True, default='')
	correo_electronico = models.CharField(max_length=255, blank=True, default='')
	ubicacion_en_la_camara = models.CharField(max_length=255, blank=True, default='')
	suplente = models.CharField(max_length=255, blank=True, default='')
	toma_deprotesta = models.CharField(max_length=255, blank=True, default='')
	fecha_de_nacimiento = models.DateTimeField()
	entidad_de_nacimiento = models.CharField(max_length=255, blank=True, default='')
	distrito = models.CharField(max_length=255, blank=True, default='')
	entidad = models.CharField(max_length=255, blank=True, default='')
	ciudad_de_nacimiento = models.CharField(max_length=255, blank=True, default='')
	principio_deeleccion = models.CharField(max_length=255, blank=True, default='')
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now_add=True)


class Meta:
	ordering = ('created_at',)
	db_table = 'representatives'