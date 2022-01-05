from django.utils.translation import gettext as _
from enums_test import EnumsTest


class TestRecordingContext(EnumsTest):
    entity = 'thematic'
    title = _("Thématique")
    data = [
        {"id":"1", "name":"danse", "notes":"Notes danse"}
    ]
    new_data = {"name":"récit", "notes":"Notes récit"}
