# -*- coding: utf-8 -*-

from rest_framework import serializers
from rest_framework.validators import UniqueValidator
from ..models.legal_rights import LegalRights as LegalRightsModel


class LegalRightsSerializer(serializers.ModelSerializer):
    """
    Common legal rights for all recording_context actions
    """

    name = serializers.CharField(
        required=True,
        validators=[UniqueValidator(queryset=LegalRightsModel.objects.all())]
        )
    notes = serializers.CharField(required=False, allow_blank=True)

    class Meta:
        model = LegalRightsModel
        fields = '__all__'
