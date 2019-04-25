import json

from rest_framework import serializers, viewsets
from merchandise.models import Product, products
from rest_framework.response import Response


# Serializers define the API representation.
class ProductViewSet(viewsets.ViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    def list(self, request):
        return Response([o.__dict__ for o in products])
