# -*- coding: utf-8 -*-

from rest_framework import serializers

from ..models.recording_context import RecordingContext as RecordingContextModel  # noqa


class RecordingContextSerializer(serializers.ModelSerializer):
    """
    Common serializer for all recording_context actions
    """

    name = serializers.CharField(required=True)
    notes = serializers.CharField(required=False, allow_blank=True)

    class Meta:
        model = RecordingContextModel
        fields = '__all__'
