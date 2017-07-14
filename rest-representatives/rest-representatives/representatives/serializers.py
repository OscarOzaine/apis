from models import Representatives
from rest_framework import serializers

class RepresentativesSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Representatives
        fields = (
        	'id', 'nombre', 'slug', 'zona',
        	'estatus', 'ultimo_grado_de_estudios', 'partido', 'telefono_en_camara',
        	'preparacion_academica', 'correo_electronico', 'ubicacion_en_la_camara', 'suplente',
        	'toma_deprotesta', 'fecha_de_nacimiento', 'entidad_de_nacimiento', 'distrito',
        	'entidad', 'ciudad_de_nacimiento', 'created_at', 'updated_at',
        	'principio_deeleccion'
        )