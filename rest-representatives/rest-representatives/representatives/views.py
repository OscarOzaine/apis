from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from serializers import RepresentativesSerializer
from models import Representatives

class RepresentativesViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Representatives.objects.all()
    serializer_class = RepresentativesSerializer
    http_method_names = ['get']