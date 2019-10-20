# -*- coding: utf-8 -*-

from rest_framework import serializers

from ..models.legal_rights import LegalRights as LegalRightsModel


class LegalRightsSerializer(serializers.ModelSerializer):
    """
    Common legal rights for all recording_context actions
    """

    name = serializers.CharField(required=True)
    notes = serializers.CharField(required=False, allow_blank=True)

    class Meta:
        model = LegalRightsModel
        fields = '__all__'
