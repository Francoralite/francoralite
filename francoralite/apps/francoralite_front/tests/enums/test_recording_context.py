from django.utils.translation import gettext as _
from enums_test import EnumsTest


class TestRecordingContext(EnumsTest):
    entity = 'recording_context'
    title = _("Contexte d’enregistrement")
    data = [
        {"id":"1", "name":"collectage", "notes":"collectage"},
        {"id":"2", "name":"bal", "notes":"bal"},
        {"id":"3", "name":"enquête", "notes":"enquête"},
    ]
    new_data = {"name":"spectacle", "notes":"Notes spectacle"}
    