from rest_framework import status
from rest_framework.exceptions import ValidationError
from rest_framework.views import exception_handler


def custom_exception_handler(exc, context):
    if isinstance(exc, ValidationError) and 'unique' in exc.get_codes().get('code', []):
        exc.status_code = status.HTTP_409_CONFLICT
    return exception_handler(exc, context)
