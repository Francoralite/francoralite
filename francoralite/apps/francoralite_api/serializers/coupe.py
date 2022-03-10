# -*- coding: utf-8 -*-

from rest_framework import serializers
from rest_framework.validators import UniqueValidator

from ..models.coupe import Coupe as CoupeModel


class CoupeSerializer(serializers.ModelSerializer):
    """
    Common serializer for all coupe actions
    """

    name = serializers.CharField(
        required=True,
        validators=[UniqueValidator(queryset=CoupeModel.objects.all())])
    notes = serializers.CharField(required=False, allow_blank=True)

    class Meta:
        model = CoupeModel
        fields = '__all__'
