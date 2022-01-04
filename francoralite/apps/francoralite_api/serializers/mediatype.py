# -*- coding: utf-8 -*-

from rest_framework import serializers
from rest_framework.validators import UniqueValidator
from ..models.mediatype import MediaType as MediaTypeModel


class MediaTypeSerializer(serializers.ModelSerializer):
    """
    Common serializer for all mediatype actions
    """

    name = serializers.CharField(
        required=True,
        validators=[UniqueValidator(queryset=MediaTypeModel.objects.all())]
        )
    notes = serializers.CharField(required=False, allow_blank=True)

    class Meta:
        model = MediaTypeModel
        fields = '__all__'
