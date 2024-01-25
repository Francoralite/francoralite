# -*- coding: utf-8 -*-

from rest_framework import serializers
from rest_framework.validators import UniqueValidator

from ..models.cultural_area import CulturalArea as CulturalAreaModel


class CulturalAreaSerializer(serializers.ModelSerializer):
    """
    Common serializer for all cultural area actions
    """

    name = serializers.CharField(
        required=True,
        validators=[UniqueValidator(queryset=CulturalAreaModel.objects.all())])
    geojson = serializers.CharField(required=False, allow_blank=True)

    class Meta:
        model = CulturalAreaModel
        fields = '__all__'
