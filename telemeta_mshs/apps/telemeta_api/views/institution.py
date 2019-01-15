from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from ..models.institution import Institution as InstitutionModel
from ..serializers.institution import InstitutionSerializer


class InstitutionViewSet(viewsets.ModelViewSet):
    """
    Institution management
    """

    queryset = InstitutionModel.objects.all()
    serializer_class = InstitutionSerializer
    permission_classes = (IsAuthenticatedOrReadOnly,)
