from rest_framework import viewsets
from ..models.recording_context import RecordingContext as RecordingContextModel
from ..serializers.recording_context import RecordingContextSerializer


class RecordingContextViewSet(viewsets.ModelViewSet):
    """
    RecordingContext management
    """

    queryset = RecordingContextModel.objects.all()
    serializer_class = RecordingContextSerializer

    keycloak_scopes = {
        'GET': 'recording_context:view',
        'POST': 'recording_context:add',
        'PATCH': 'recording_context:update',
        'PUT': 'recording_context:update',
        'DELETE': 'recording_context:delete'
    }
