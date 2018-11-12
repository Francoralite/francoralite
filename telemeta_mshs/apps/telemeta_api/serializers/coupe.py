# -*- coding: utf-8 -*-

from rest_framework import serializers

from ..models.coupe import Coupe as CoupeModel


class CoupeSerializer(serializers.ModelSerializer):
    """
    Common serializer for all coupe actions
    """

    value = serializers.CharField(required=True)
    notes = serializers.CharField()

    class Meta:
        model = CoupeModel
        fields = '__all__'