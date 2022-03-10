from django.utils.translation import gettext as _
from enums_test import EnumsTest


class TestRecordingContext(EnumsTest):
    entity = 'thematic'
    title = _("Thématique")
    data = [
        {"id":"1", "name":"danse", "notes":"Notes danse"},
        {"id":"2", "name":"récit", "notes":""},
    ]
    new_data = {"name":"répertoire de chansons", "notes":"Notes répertoire"}
