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
    roles = serializers.MultipleChoiceField( choices=ROLES )
    birth_date = serializers.DateField( allow_null=True )
    # FIXIT ----
    #birth_location = ForeignKey('Location', related_name='birth_location', verbose_name=_('birth location'), blank=True, null=True, on_delete=models.SET_NULL)
    birth_location = serializers.StringRelatedField()
    death_date = serializers.DateField( allow_null=True )
    # FIXIT ----
    #death_location = ForeignKey('Location',related_name='death_location', verbose_name=_('death location'), blank=True, null=True, on_delete=models.SET_NULL)
    death_location = serializers.StringRelatedField()
    biography = serializers.CharField( allow_null=True, allow_blank=True )
    uri = serializers.URLField( allow_null=True, allow_blank=True)



    class Meta:
        model = AuthorityModel
        fields = '__all__'
