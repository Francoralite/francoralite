# -*- coding: utf-8 -*-

from rest_framework import serializers

from ..models.authority import Authority as AuthorityModel


class AuthoritySerializer(serializers.ModelSerializer):
    """
    Common serializer for all authority actions
    """

    last_name = serializers.CharField(required=True)
    first_name = serializers.CharField()
    civilite = serializers.CharField()
    alias = serializers.CharField()
    ROLES = (
        ('ENQ', 'Enquêteur'),
        ('INF', 'Informateur'),
        ('AUT', 'Auteur'),
        ('CMP', 'Compositeur'),
        ('EDT', 'Editeur')
    )
    roles = serializers.CharField()
    birth_date = serializers.DateField(allow_null=True)
    birth_location = serializers.StringRelatedField()
    death_date = serializers.DateField(allow_null=True)
    death_location = serializers.StringRelatedField()
    biography = serializers.CharField(allow_null=True, allow_blank=True)
    uri = serializers.URLField(allow_null=True, allow_blank=True)

    class Meta:
        model = AuthorityModel
        fields = '__all__'
