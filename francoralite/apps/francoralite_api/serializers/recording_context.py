# -*- coding: utf-8 -*-

from rest_framework import serializers
from rest_framework.validators import UniqueValidator
from ..models.recording_context import (
    RecordingContext as RecordingContextModel )


class RecordingContextSerializer(serializers.ModelSerializer):
    """
    Common serializer for all recording_context actions
    """

    name = serializers.CharField(
        required=True,
        validators=[UniqueValidator(queryset=RecordingContextModel.objects.all())]
        )
    notes = serializers.CharField(required=False, allow_blank=True)

    class Meta:
        model = RecordingContextModel
        fields = '__all__'
