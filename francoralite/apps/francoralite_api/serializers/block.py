# -*- coding: utf-8 -*-

from rest_framework import serializers

from ..models.block import Block as BlockModel


class BlockSerializer(serializers.ModelSerializer):
    """
    Common serializer for all block actions
    """
    type = serializers.CharField(max_length=1, required=True, allow_blank=False, allow_null=True)
    title = serializers.CharField(max_length=255, required=True, allow_blank=False)
    content = serializers.CharField(required=False, allow_blank=True, allow_null=True)
    order = serializers.IntegerField(required=True)
    show = serializers.BooleanField(required=True)

    class Meta:
        model = BlockModel
        fields = '__all__'
