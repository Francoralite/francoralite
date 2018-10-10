# -*- coding: utf-8 -*-

from rest_framework import serializers

from ..models.authority import Authority as AuthorityModel


class AuthoritySerializer(serializers.ModelSerializer):
    """
    Common serializer for all authority actions
    """

    last_name = serializers.CharField(required=True)
    first_name = serializers.CharField(allow_blank=True)
    civilite = serializers.CharField(allow_blank=True)
    alias = serializers.CharField(allow_blank=True)
    ROLES = (
        ('ENQ', 'Enquêteur'),
        ('INF', 'Informateur'),
        ('AUT', 'Auteur'),
        ('CMP', 'Compositeur'),
        ('EDT', 'Editeur')
    )
    roles = serializers.CharField(allow_blank=True)
    birth_date = serializers.DateField(required=False)
    birth_location = serializers.StringRelatedField()
    death_date = serializers.DateField(required=False)
    death_location = serializers.StringRelatedField()
    biography = serializers.CharField(allow_null=True, allow_blank=True)
    uri = serializers.URLField(allow_null=True, allow_blank=True)

    class Meta:
        model = AuthorityModel
        fields = '__all__'
