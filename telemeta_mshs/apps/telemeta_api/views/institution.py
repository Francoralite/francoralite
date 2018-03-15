from rest_framework import viewsets
from ..models.institution import Institution as InstitutionModel
from ..serializers.institution import InstitutionSerializer


class InstitutionViewSet(viewsets.ModelViewSet):
    """
    Institution management
    """

    queryset = InstitutionModel.objects.all()
    serializer_class = InstitutionSerializer
