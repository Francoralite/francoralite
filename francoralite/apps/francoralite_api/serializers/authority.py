# -*- coding: utf-8 -*-

from rest_framework import serializers

from ..models.authority import Authority as AuthorityModel
from .location_gis import LocationGisSerializer
from .asymetric_related_field import AsymetricRelatedField


class AuthoritySerializer(serializers.ModelSerializer):
    """
    Common serializer for all authority actions
    """
    last_name = serializers.CharField(allow_blank=True, required=False)
    birth_date = serializers.DateField(required=False)
    birth_location = AsymetricRelatedField.from_serializer(
        LocationGisSerializer, kwargs={'required': False, 'allow_null': True})
    death_date = serializers.DateField(required=False)
    death_location = AsymetricRelatedField.from_serializer(
        LocationGisSerializer, kwargs={'required': False, 'allow_null': True})
    biography = serializers.CharField(allow_null=True,
                                      allow_blank=True, required=False)

    class Meta:
        model = AuthorityModel
        fields = '__all__'
