# -*- coding: utf-8 -*-

from rest_framework import serializers
from rest_framework.validators import UniqueValidator

from ..models.civility import Civility as CivilityModel


class CivilitySerializer(serializers.ModelSerializer):
    """
    Common serializer for all civility actions
    """

    name = serializers.CharField(
        required=True,
        validators=[UniqueValidator(queryset=CivilityModel.objects.all())])

    class Meta:
        model = CivilityModel
        fields = '__all__'
