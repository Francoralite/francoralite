from rest_framework import viewsets
from ..models.authority import Authority as AuthorityModel
from ..serializers.authority import AuthoritySerializer


class AuthorityViewSet(viewsets.ModelViewSet):
    """
    Authority management
    """

    queryset = AuthorityModel.objects.all()
    serializer_class = AuthoritySerializer
