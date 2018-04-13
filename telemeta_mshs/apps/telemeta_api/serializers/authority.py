# -*- coding: utf-8 -*-

from rest_framework import serializers

from ..models.authority import Authority as AuthorityModel


class AuthoritySerializer(serializers.ModelSerializer):
    """
    Common serializer for all authority actions
    """


    last_name = serializers.CharField(required=True)
    first_name = serializers.CharField()
    civilite =  serializers.CharField()
    alias =  serializers.CharField()
    ROLES = (
        ('ENQ','Enquêteur'),
        ('INF','Informateur'),
        ('AUT','Auteur'),
        ('CMP','Compositeur'),
        ('EDT','Editeur')
    )
    roles = serializers.MultipleChoiceField(choices=ROLES)
    birth_date = serializers.DateField(null=True)
    # FIXIT ----
    #birth_location = ForeignKey('Location', related_name='birth_location', verbose_name=_('birth location'), blank=True, null=True, on_delete=models.SET_NULL)
    death_date = serializers.DateField( null=True )
    # FIXIT ----
    #death_location = ForeignKey('Location',related_name='death_location', verbose_name=_('death location'), blank=True, null=True, on_delete=models.SET_NULL)
    biography = serializers.TextField( null=True, blank=True )
    uri = serializers.URLField(null=True, blank=True)



    class Meta:
        model = AuthorityModel
        fields = '__all__'
