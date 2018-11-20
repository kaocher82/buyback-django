from rest_framework.viewsets import ReadOnlyModelViewSet
from rest_framework import filters

from .models import Inspection
from .serializers import InspectionSerializer


class InspectionViewSet(ReadOnlyModelViewSet):
    serializer_class = InspectionSerializer
    queryset = Inspection.objects.all()
    filter_backends = (filters.SearchFilter,)
    search_fields = ('address',)
