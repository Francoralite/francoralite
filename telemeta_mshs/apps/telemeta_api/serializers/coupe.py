# -*- coding: utf-8 -*-

from rest_framework import serializers

from ..models.coupe import Coupe as CoupeModel


class CoupeSerializer(serializers.ModelSerializer):
    """
    Common serializer for all coupe actions
    """

    name = serializers.CharField(required=True)
    notes = serializers.CharField(required=False)

    class Meta:
        model = CoupeModel
        fields = '__all__'
