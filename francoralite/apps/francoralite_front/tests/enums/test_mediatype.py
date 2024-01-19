from django.utils.translation import gettext as _
from enums_test import EnumsTest


class TestMediatype(EnumsTest):
    entity = 'mediatype'
    title = _("Type de média")
    data = [
        {"id":"1", "name":"cassette audio", "notes":"cassette audio"},
        {"id":"2", "name":"bande dat", "notes": "bande DAT"},
        {"id":"3", "name":"Son uniquement", "notes": "Archive sonore"}
    ]
    new_data = {"name":"cd", "notes":"disque laser"}
