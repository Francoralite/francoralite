# -*- coding: utf-8 -*-
# source : http://sametmax.com/accepter-un-id-mais-retourner-un-objet-pour-les-liens-de-django-rest-framework/ # noqa

from collections import OrderedDict
from rest_framework import serializers


class AsymetricRelatedField(serializers.PrimaryKeyRelatedField):

    # en lecture, je veux l'objet complet, pas juste l'id
    def to_representation(self, value):
        # le self.serializer_class.serializer_class est redondant
        # mais obligatoire
        return self.serializer_class(value).data

    # petite astuce perso et pas obligatoire pour permettre de taper moins
    # de code: lui faire prendre le queryset du model du serializer
    # automatiquement. Je suis lazy
    def get_queryset(self):
        if self.queryset:
            return self.queryset
        return self.serializer_class.Meta.model.objects.all()

    # Get choices est utilisé par l'autodoc DRF et s'attend à ce que
    # to_representation() retourne un ID ce qui fait tout planter. On
    # réécrit le truc pour utiliser item.pk au lieu de to_representation()
    def get_choices(self, cutoff=None):
        queryset = self.get_queryset()
        if queryset is None:
            return {}

        if cutoff is not None:
            queryset = queryset[:cutoff]

        return OrderedDict([
            (
                item.pk,
                self.display_value(item)
            )
            for item in queryset
        ])

    # DRF saute certaines validations quand il n'y a que l'id, et comme ce
    # n'est pas le cas ici, tout plante. On désactive ça.
    def use_pk_only_optimization(self):
        return False

    # Un petit constructeur pour générer le field depuis un serializer. lazy,
    # lazy, lazy...
    @classmethod
    def from_serializer(cls, serializer, name=None, args=(), kwargs={}):
        if name is None:
            name = str({serializer.__name__})+"AsymetricAutoField"

        return type(name, (cls,),
                    {"serializer_class": serializer})(*args, **kwargs)
