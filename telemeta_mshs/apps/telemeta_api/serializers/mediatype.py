# -*- coding: utf-8 -*-

from rest_framework import serializers

from ..models.mediatype import MediaType as MediaTypeModel


class MediaTypeSerializer(serializers.ModelSerializer):
    """
    Common serializer for all mediatype actions
    """

    value = serializers.CharField(required=True)
    notes = serializers.CharField()

    class Meta:
        model = MediaTypeModel
        fields = '__all__'
