# -*- coding: utf-8 -*-

from rest_framework import serializers

from ..models.mediatype import MediaType as MediaTypeModel


class MediaTypeSerializer(serializers.ModelSerializer):
    """
    Common serializer for all mediatype actions
    """

    name = serializers.CharField(required=True)
    notes = serializers.CharField(required=False)

    class Meta:
        model = MediaTypeModel
        fields = '__all__'
