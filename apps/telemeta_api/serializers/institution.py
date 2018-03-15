# -*- coding: utf-8 -*-

from rest_framework import serializers

from ..models.institution import Institution as InstitutionModel


class InstitutionSerializer(serializers.ModelSerializer):
    """
    Common serializer for all Institution actions
    """

    name = serializers.CharField(required=True)
    notes = serializers.TextField()

    class Meta:
        model = InstitutionModel
        fields = '__all__'
