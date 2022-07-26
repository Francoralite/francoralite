from django.core.exceptions import ValidationError as DjangoValidationError
from django.http.response import JsonResponse

from rest_framework import status
from rest_framework.exceptions import ValidationError
from rest_framework.views import exception_handler


def custom_exception_handler(exc, context):
    if isinstance(exc, DjangoValidationError):
        return JsonResponse({'type': 'validation', 'fields': exc.message_dict}, status=400)
    if isinstance(exc, ValidationError) and any(
        'unique' in err_codes for err_codes in exc.get_codes().values()):
        exc.status_code = status.HTTP_409_CONFLICT
    return exception_handler(exc, context)
