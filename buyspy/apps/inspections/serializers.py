from rest_framework.serializers import ModelSerializer

from .models import Inspection


class InspectionSerializer(ModelSerializer):
    class Meta:
        model = Inspection
        exclude = ('description_markup_type', '_description_rendered')
