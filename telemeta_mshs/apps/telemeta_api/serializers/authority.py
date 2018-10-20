# -*- coding: utf-8 -*-

from rest_framework import serializers

from ..models.authority import Authority as AuthorityModel
from ..models.location import Location as LocationModel


class AuthoritySerializer(serializers.ModelSerializer):
    """
    Common serializer for all authority actions
    """

    civility = serializers.CharField(allow_blank=True, required=False)
    birth_date = serializers.DateField(required=False)
    birth_location = serializers.PrimaryKeyRelatedField(
        queryset=LocationModel.objects.all(), required=False)
    death_date = serializers.DateField(required=False)
    death_location = serializers.PrimaryKeyRelatedField(
        queryset=LocationModel.objects.all(), required=False)
    biography = serializers.CharField(allow_null=True,
                                      allow_blank=True, required=False)

    class Meta:
        model = AuthorityModel
        fields = '__all__'
